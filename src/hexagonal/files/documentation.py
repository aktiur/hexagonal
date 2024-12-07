import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import urljoin

import dvc.api
import tomlkit
import yaml

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


def get_files(directory: Path, extensions):
    return [
        dirpath / filename
        for dirpath, _, filenames in directory.walk()
        for filename in filenames
        if any(filename.endswith(f".{ext}") for ext in extensions)
    ]


def get_dvc_file(dvc_path):
    with open(dvc_path, "r") as fd:
        return yaml.safe_load(fd)


def get_project_config():
    with open("pyproject.toml", "r") as fd:
        return tomlkit.load(fd)


def convert_s3_url_to_http(url, config):
    s3_buckets = config["tool"]["hexagonal"]["remotes"]
    bucket, path = re.match(r"^s3://([^/]+)(.*)$", url).groups()
    return urljoin(s3_buckets[bucket], path)


def update_spec():
    config = get_project_config()

    with open("data/spec.toml") as fd:
        doc = tomlkit.load(fd)

    data_dir = Path("data")

    sources_dvc_files = get_files(data_dir / "01_raw", ["dvc"])
    productions_files = [
        *get_files(data_dir / "02_clean", DATA_EXTENSIONS),
        *get_files(data_dir / "03_main", DATA_EXTENSIONS),
    ]

    sources_table = doc.setdefault("sources", tomlkit.table())
    for path in sources_dvc_files:
        dvc_metadata = get_dvc_file(path)
        filename = path.parent / dvc_metadata["outs"][0]["path"]

        file_table = sources_table.setdefault(str(filename), tomlkit.table())

        defaults = {
            "nom": filename.stem,
            "description": tomlkit.string("\n", multiline=True),
        }
        for k, v in defaults.items():
            file_table.setdefault(k, v)

        if dvc_metadata.get("deps"):
            file_table["url"] = dvc_metadata["deps"][0]["path"]

    productions_table = doc.setdefault("productions", tomlkit.table())

    for path in productions_files:
        file_table = productions_table.setdefault(str(path), tomlkit.table())
        defaults = {
            "nom": path.stem,
            "description": tomlkit.string("\n", multiline=True),
            "type": path.suffix[1:],
        }

        for k, v in defaults.items():
            file_table.setdefault(k, v)

        s3_url = dvc.api.get_url(str(path))
        http_url = convert_s3_url_to_http(s3_url, config)

        file_table.update(
            {
                "url": http_url,
                "s3_url": s3_url,
            }
        )

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
