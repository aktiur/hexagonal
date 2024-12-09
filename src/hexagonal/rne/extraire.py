import csv
import re
import sys
from pathlib import Path

import click
from glom import glom, Iter, T

from hexagonal.annuaire.nettoyer import spec_conseils_departementaux
from hexagonal.utils import date_francaise_vers_iso


NUMERO_RE = re.compile(r"\d+")


def code_secteur(elu):
    numero_secteur = NUMERO_RE.search(elu["Libellé du secteur"]).group(0).zfill(2)
    return f"{elu['Code de la commune']}SR{numero_secteur}"


spec_conseiller_arrondissement = {
    "code_commune": "Code de la commune",
    "code_secteur": code_secteur,
    "nom": "Nom de l'élu",
    "prenom": "Prénom de l'élu",
    "sexe": "Code sexe",
    "date_naissance": "Date de naissance",
    "lieu_naissance": "Lieu de naissance",
    "csp": "Code de la catégorie socio-professionnelle",
    "date_debut_mandat": ("Date de début du mandat", date_francaise_vers_iso),
    "fonction": "Libellé de la fonction",
    "date_debut_fonction": ("Date de début de la fonction", date_francaise_vers_iso),
    "nuance": "Code de la nuance politique",
}

spec_conseiller_municipal = {
    "code_departement": ("Code du département", T.zfill(2)),
    "code_collectivite_sp": "Code de la collectivité à statut particulier",
    "code_commune": ("Code de la commune", T.zfill(5)),
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


spec_conseiller_departemental = {
    "code_departement": ("Code du département", T.zfill(2)),
    "code_canton": ("Code du canton", T.zfill(4)),
    "nom": "Nom de l'élu",
    "prenom": "Prénom de l'élu",
    "sexe": "Code sexe",
    "date_naissance": ("Date de naissance", date_francaise_vers_iso),
    "csp": "Code de la catégorie socio-professionnelle",
    "date_debut_mandat": ("Date de début du mandat", date_francaise_vers_iso),
    "fonction": "Libellé de la fonction",
    "date_debut_fonction": ("Date de début de la fonction", date_francaise_vers_iso),
}

spec_conseiller_regional = {
    "code_region": ("Code de la région", T.zfill(2)),
    "code_departement": ("Code de la section départementale", T.zfill(2)),
    "nom": "Nom de l'élu",
    "prenom": "Prénom de l'élu",
    "sexe": "Code sexe",
    "date_naissance": ("Date de naissance", date_francaise_vers_iso),
    "csp": "Code de la catégorie socio-professionnelle",
    "date_debut_mandat": ("Date de début du mandat", date_francaise_vers_iso),
    "fonction": "Libellé de la fonction",
    "date_debut_fonction": ("Date de début de la fonction", date_francaise_vers_iso),
}

SPECS = {
    "conseillers_arrondissement": spec_conseiller_arrondissement,
    "conseillers_municipaux": spec_conseiller_municipal,
    "conseillers_departementaux": spec_conseiller_departemental,
    "conseillers_regionaux": spec_conseiller_regional,
}


def extraire(in_path, out_path, spec):
    with (
        open(in_path, "r", newline="") as in_fd,
        open(out_path, "w", newline="") as out_fd,
    ):
        r = csv.DictReader(in_fd, delimiter=";")
        w = csv.DictWriter(out_fd, fieldnames=list(spec.keys()))

        w.writeheader()
        w.writerows(glom(r, Iter(spec)))


@click.command()
@click.argument(
    "src_dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
)
@click.argument(
    "dest_dir", type=click.Path(file_okay=False, dir_okay=True, path_type=Path)
)
@click.argument("type_mandat", type=click.Choice(list(SPECS.keys())))
def run(src_dir, dest_dir, type_mandat):
    dest_dir.mkdir(exist_ok=True, parents=True)

    extraire(
        src_dir / f"{type_mandat}.csv",
        dest_dir / f"{type_mandat}.csv",
        SPECS[type_mandat],
    )


if __name__ == "__main__":
    run()
