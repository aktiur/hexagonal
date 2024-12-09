import csv
import sys
from pathlib import Path
from zipfile import Path as ZPath, ZipFile

import click
from glom import glom

from hexagonal.cog.type_nom import TYPES_NOMS

ANNEE = 2024


def article(entite):
    return TYPES_NOMS[int(entite["TNCC"])].article


def charniere(entite):
    return TYPES_NOMS[int(entite["TNCC"])].charniere


spec_departement = {
    "code_departement": "DEP",
    "code_region": "REG",
    "code_chef_lieu": "CHEFLIEU",
    "type_nom": "TNCC",
    "nom": "NCCENR",
}

spec_com = {
    "code_com": "COMER",
    "type_nom": "TNCC",
    "nom": "NCCENR",
    "article": article,
    "charniere": charniere,
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
    "article": article,
    "charniere": charniere,
}

spec_commune_com = {
    "code_commune": "COM_COMER",
    "code_com": "COMER",
    "nature_zonage": "NATURE_ZONAGE",
    "type_nom": "TNCC",
    "nom": "NCCENR",
    "article": article,
    "charniere": charniere,
}

spec_commune_historique = {
    "code_commune": "COM",
    "type_nom": "TNCC",
    "nom": "NCCENR",
    "article": article,
    "charniere": charniere,
    "date_debut": "DATE_DEBUT",
    "date_fin": "DATE_FIN",
}


fichiers_cog = [
    (f"v_commune_{ANNEE}", "communes", spec_commune),
    (f"v_commune_comer_{ANNEE}", "communes_com", spec_commune_com),
    (f"v_departement_{ANNEE}", "departements", spec_departement),
    (f"v_comer_{ANNEE}", "com", spec_com),
    (f"v_commune_depuis_1943", "communes_historiques", spec_commune_historique),
]


def extraire(in_path, out_path, spec):
    with in_path.open("r") as fd:
        r = csv.DictReader(fd)
        elems = glom(r, [spec])

    with out_path.open("w", newline="") as fd:
        w = csv.DictWriter(fd, fieldnames=elems[0].keys())
        w.writeheader()
        w.writerows(elems)


@click.command()
@click.argument(
    "archive_path", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.argument(
    "dest_dir", type=click.Path(file_okay=False, dir_okay=True, path_type=Path)
)
def run(archive_path, dest_dir):
    dest_dir.mkdir(exist_ok=True, parents=True)

    with ZipFile(archive_path) as archive:
        archive_root = ZPath(archive)

        for src, dest, spec in fichiers_cog:
            extraire(
                archive_root / f"{src}.csv",
                dest_dir / f"{dest}.csv",
                spec,
            )


if __name__ == "__main__":
    run()
