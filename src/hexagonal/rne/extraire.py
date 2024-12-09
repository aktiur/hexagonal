import csv
import sys
from pathlib import Path

from glom import glom, Iter

from hexagonal.utils import date_francaise_vers_iso

spec_conseiller_municipal = {
    "code_departement": "Code du département",
    "code_collectivite_sp": "Code de la collectivité à statut particulier",
    "code_commune": "Code de la commune",
    "nom": "Nom de l'élu",
    "prenom": "Prénom de l'élu",
    "sexe": "Code sexe",
    "date_naissance": ("Date de naissance", date_francaise_vers_iso),
    "csp": "Code de la catégorie socio-professionnelle",
    "date_debut_mandat": ("Date de début du mandat", date_francaise_vers_iso),
    "fonction": "Libellé de la fonction",
    "date_debut_fonction": ("Date de début de la fonction", date_francaise_vers_iso),
    "nationalite": "Code nationalité",
}


types_mandats = {"conseillers_municipaux": spec_conseiller_municipal}


def extraire(in_path, out_path, spec):
    with (
        open(in_path, "r", newline="") as in_fd,
        open(out_path, "w", newline="") as out_fd,
    ):
        r = csv.DictReader(in_fd, delimiter=";")
        w = csv.DictWriter(out_fd, fieldnames=list(spec.keys()))

        w.writeheader()
        w.writerows(glom(r, Iter(spec)))


def run():
    in_path, out_path = sys.argv[1:]

    in_path, out_path = Path(in_path), Path(out_path)

    for type_mandat, spec in types_mandats.items():
        extraire(in_path / f"{type_mandat}.csv", out_path / f"{type_mandat}.csv", spec)


if __name__ == "__main__":
    run()
