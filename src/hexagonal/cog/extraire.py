import csv
import sys
from pathlib import Path
from zipfile import Path as ZPath, ZipFile

from glom import glom
from markdown_it.rules_inline import newline

ANNEE = 2024


spec_departement = {
    "code_departement": "DEP",
    "code_region": "REG",
    "code_chef_lieu": "CHEFLIEU",
    "type_nom": "TNCC",
    "nom": "NCCENR",
}

spec_commune = {
    "code_commune": "COM",
    "type_commune": "TYPECOM",
    "code_region": "REG",
    "code_departement": "DEP",
    "code_collectivite_departementale": "CTCD",
    "code_arrondissement": "ARR",
    "code_canton": "CAN",
    "code_commune_parent": "COMPARENT",
    "type_nom": "TNCC",
    "nom": "NCCENR",
}


entites = {
    "departement": spec_departement,
    "commune": spec_commune,
}


def extraire(in_path, out_path, spec):
    with in_path.open("r") as fd:
        r = csv.DictReader(fd)
        elems = glom(r, [spec])

    with out_path.open("w", newline="") as fd:
        w = csv.DictWriter(fd, fieldnames=elems[0].keys())
        w.writeheader()
        w.writerows(elems)


def extraire_departements(archive, out_path):
    with (ZPath(archive) / "v_departement_2024.csv").open("r") as fd:
        r = csv.DictReader(fd)

        departements = glom(r, [spec_departement])

    with open(out_path, "w", newline="") as fd:
        w = csv.DictWriter(fd, departements[0].keys())
        w.writeheader()
        w.writerows(departements)


def run():
    archive_path, out_path = sys.argv[1:]
    out_path = Path(out_path)

    with ZipFile(archive_path) as archive:
        archive_root = ZPath(archive)

        for entite, spec in entites.items():
            extraire(
                archive_root / f"v_{entite}_{ANNEE}.csv",
                out_path / f"{entite}s.csv",
                spec,
            )


if __name__ == "__main__":
    run()
