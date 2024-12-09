import csv

import tomlkit

from hexagonal.files.dvc_files import get_dvc_files, OUTPUT_TYPES

FIELDS_ORDER = [
    "nom",
    "type",
    "description",
    "format",
    "url",
    "s3_url",
    "source_url",
    "info_url",
    "editeur",
    "licence",
]


def update_spec():

    with open("spec.toml") as fd:
        orig_doc = tomlkit.load(fd)

    new_doc = tomlkit.table()

    data_files = sorted(get_dvc_files())

    for file in sorted(data_files):
        orig_table = orig_doc.get(str(file), {})

        defaults = {
            "nom": file.path.stem,
            "description": tomlkit.string("\n", multiline=True),
            "format": file.default_format,
            "type": file.default_type,
        }

        overwrites = {
            "url": file.http_url,
            "s3_url": file.s3_url,
        }

        data_deps = tomlkit.array()
        data_deps.extend(str(p) for p in file.data_deps)
        if data_deps:
            overwrites["deps"] = data_deps.multiline(len(data_deps) > 1)

        if file.source_url:
            overwrites["source_url"] = file.source_url

        # l'ordre est essentiel
        values = {
            **defaults,
            **orig_table,
            **overwrites,
        }

        if values["format"] == "csv" and values["type"] in OUTPUT_TYPES:
            try:
                with open(file.path, "r", newline="") as fd:
                    r = csv.reader(fd)
                    colonnes = next(r)
            except (csv.Error, UnicodeDecodeError):
                pass
            else:
                original_colonnes = orig_table.get("colonnes", {})
                colonnes_table = tomlkit.table()
                for colonne in colonnes:
                    colonnes_table[colonne] = original_colonnes.get(
                        colonne, tomlkit.table()
                    )

                    colonnes_defaults = {
                        "nom": colonne,
                        "description": tomlkit.string("\n", multiline=True),
                        "type": "str",
                    }

                    for k, v in colonnes_defaults.items():
                        colonnes_table[colonne].setdefault(k, v)

                values["colonnes"] = colonnes_table

        fields = [
            *[f for f in FIELDS_ORDER if f in values],
            *[f for f in values if f not in FIELDS_ORDER],
        ]

        table = tomlkit.table()
        table.update(
            {**{f: None for f in fields}, **values}  # pour les champs dans l'ordre
        )
        new_doc[str(file)] = table

    with open("spec.toml", "w") as fd:
        tomlkit.dump(new_doc, fd)


if __name__ == "__main__":
    update_spec()
