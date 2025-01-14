import csv
import tomllib
from mimetypes import guess_type

import tomli_w

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

        mimetype, encoding = guess_type(file.path)
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
            except (csv.Error, UnicodeDecodeError):
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

    with open("spec.toml", "wb") as fd:
        tomli_w.dump(new_spec, fd, multiline_strings=True)


if __name__ == "__main__":
    update_spec()
