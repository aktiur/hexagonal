import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

import tomlkit
from tomlkit.items import Table

DATA_EXTENSIONS = ["json", "csv"]


@dataclass
class Colonne:
    id: str
    label: str
    description: str
    type: str


@dataclass
class CSV:
    path: str
    label: str
    description: str
    columns: List[Colonne]


def get_data_files(directory: Path):
    return [
        dirpath / filename
        for dirpath, _, filenames in directory.walk()
        for filename in filenames
        if any(filename.endswith(f".{ext}") for ext in DATA_EXTENSIONS)
    ]


def update_spec():
    with open("data/spec.toml") as fd:
        doc = tomlkit.load(fd)

    data_dir = Path("data")

    data_files = get_data_files(data_dir / "02_clean") + get_data_files(
        data_dir / "03_main"
    )

    for path in data_files:
        file_table = doc.setdefault(str(path), tomlkit.table())
        defaults = {
            "nom": path.stem,
            "description": tomlkit.string("\n", multiline=True),
            "type": path.suffix[1:],
        }

        for k, v in defaults.items():
            file_table.setdefault(k, v)

        if file_table["type"] == "csv":
            with open(path, "r", newline="") as fd:
                r = csv.reader(fd)
                colonnes = next(r)

            original_colonnes = file_table.get("colonnes", {})
            colonnes_table = tomlkit.table()
            for colonne in colonnes:
                colonnes_table[colonne] = original_colonnes.get(
                    colonne, tomlkit.table()
                )

                defaults = {
                    "nom": colonne,
                    "description": tomlkit.string("\n", multiline=True),
                    "type": "str",
                }

                for k, v in defaults.items():
                    colonnes_table[colonne].setdefault(k, v)

            file_table["colonnes"] = colonnes_table

    with open("data/spec.toml", "w") as fd:
        tomlkit.dump(doc, fd)


if __name__ == "__main__":
    update_spec()
