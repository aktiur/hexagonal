import csv
import mimetypes
import tomllib

import pyarrow.parquet as pq
import tomli_w
from pyarrow import ArrowException

from hexagonal.files.dvc_files import get_dvc_files
from hexagonal.files.spec import PRODUCTION_TYPES, ColonneType

FIELDS_ORDER = [
    "nom",
    "section",
    "type",
    "description",
    "mimetype",
    "encoding",
    "url",
    "s3_url",
    "source_url",
    "info_url",
    "editeur",
    "licence",
]

mimetypes.add_type(
    "application/vnd.apache.parquet",
    ".parquet",
)

PARQUET_TYPES = {
    "STRING": ColonneType.STR,
    "BYTE_ARRAY": ColonneType.STR,
    "INT8": ColonneType.INT,
    "INT16": ColonneType.INT,
    "INT32": ColonneType.INT,
    "INT64": ColonneType.INT,
}


def update_spec():
    new_spec = {}

    with open("spec.toml", "rb") as fd:
        old_spec = tomllib.load(fd)

    data_files = sorted(get_dvc_files())

    for file in data_files:
        orig_spec = old_spec.get(str(file.path), {})

        defaults = {
            "nom": file.path.stem,
            "description": "\n",
            "type": file.default_type,
        }

        mimetype, encoding = mimetypes.guess_type(file.path)
        if mimetype and encoding:
            mimetype = f"{mimetype}+{encoding}"
        elif encoding:
            mimetype = f"application/x-{encoding}"

        overwrites = {
            "url": file.http_url,
            "s3_url": file.s3_url,
            "mimetype": mimetype or "",
        }
        if file.data_deps:
            overwrites["deps"] = [str(f) for f in file.data_deps]

        file_spec = {**defaults, **orig_spec, **overwrites}

        if (
            file_spec["mimetype"] == "text/csv"
            and file_spec["type"] in PRODUCTION_TYPES
        ):
            try:
                with open(file.path, "r", newline="") as fd:
                    r = csv.reader(fd)
                    colonnes = next(r)
            except (csv.Error, UnicodeDecodeError, FileNotFoundError):
                pass
            else:
                original_colonnes = file_spec.get("colonnes", {})
                colonnes_table = {}
                for colonne in colonnes:
                    colonnes_table[colonne] = original_colonnes.get(colonne, {})

                    colonnes_defaults = {
                        "description": "",
                        "type": ColonneType.STR,
                    }

                    for k, v in colonnes_defaults.items():
                        colonnes_table[colonne].setdefault(k, v)

                file_spec["colonnes"] = colonnes_table

        fields = [
            *[f for f in FIELDS_ORDER if f in file_spec],
            *[f for f in file_spec if f not in FIELDS_ORDER],
        ]
        new_spec[str(file.path)] = {f: file_spec[f] for f in fields}

        if (
            file_spec["mimetype"] == "application/vnd.apache.parquet"
            and file_spec["type"] in PRODUCTION_TYPES
        ):
            try:
                parquet_data = pq.ParquetFile(file.path)
                columns = parquet_data.schema

                original_colonnes = file_spec.get("colonnes", {})
                colonnes_table = {}

                for colonne in columns:
                    colonnes_table[colonne.name] = original_colonnes.get(
                        colonne.name, {}
                    )

                    col_type = PARQUET_TYPES.get(
                        colonne.logical_type.type, PARQUET_TYPES[colonne.physical_type]
                    )

                    colonnes_defaults = {
                        "description": "",
                        "type": col_type,
                    }

                    for k, v in colonnes_defaults.items():
                        colonnes_table[colonne.name].setdefault(k, v)

            except ArrowException:
                pass

    with open("spec.toml", "wb") as fd:
        tomli_w.dump(new_spec, fd, multiline_strings=True)


if __name__ == "__main__":
    update_spec()
