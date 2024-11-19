import json
from zipfile import Path


def possiblement_nul(d):
    if isinstance(d, dict):
        if "@xsi:nil" in d and d["@xsi:nil"] == "true":
            return ""
        raise ValueError(f"Valeur incorrecte: {d!r}")
    return d


def json_deputees(archive):
    for deputee_file in (Path(archive) / "json" / "acteur").iterdir():
        with deputee_file.open() as fd:
            yield json.load(fd)["acteur"]


def json_organes(archive):
    for organe_file in (Path(archive) / "json" / "organe").iterdir():
        with organe_file.open() as fd:
            yield json.load(fd)["organe"]
