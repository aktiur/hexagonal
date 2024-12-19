import click
from glom import Coalesce, T

from hexagonal.codes import normalisation_code_circonscription_ministere
from hexagonal.utils import (
    date_francaise_vers_iso,
    nettoyer_avec_spec,
    iterate_csv,
    vers_booleen,
)

booleen = vers_booleen(vrai=["oui"])

spec = {
    "departement": Coalesce("Code du département", "Code département"),
    "circonscription": (
        "Code circonscription",
        normalisation_code_circonscription_ministere,
    ),
    "numero_panneau": Coalesce("N° panneau", "Numéro de panneau"),
    "numero_depot": Coalesce("N° candidat", "N° dépôt"),
    "sexe": Coalesce("Sexe candidat", "Sexe du candidat"),
    "nom": Coalesce("Nom candidat", "Nom du candidat"),
    "prenom": Coalesce("Prénom candidat", "Prénom du candidat"),
    "date_naissance": (
        Coalesce("Date naissance candidat", "Date de naissance du candidat"),
        date_francaise_vers_iso,
    ),
    "nuance": Coalesce("Nuance candidat", "Code nuance"),
    "profession": Coalesce("Profession candidat", "Profession"),
    "sortant": (
        Coalesce("Le candidat est sortant", "Sortant"),
        T.lower(),
        booleen,
    ),
    "sexe_suppleant": "Sexe remplaçant",
    "nom_suppleant": "Nom remplaçant",
    "prenom_suppleant": "Prénom remplaçant",
    "date_naissance_suppleant": (
        Coalesce(
            T[
                "Date naiss. remplaçant"
            ],  # Attention à la présence d'un . dans le nom du champ
            "Date de naissance remplaçant",
        ),
        date_francaise_vers_iso,
    ),
    "sortant_suppleant": (
        Coalesce("Le remplaçant est sortant", "Sortant remplaçant"),
        T.lower(),
        booleen,
    ),
}


@click.command()
@click.argument(
    "src_file", type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
@click.argument("dest_file", type=click.Path(file_okay=True, dir_okay=False))
@click.option("-d", "--delimiter", default=",")
@click.option("-e", "--encoding", default="utf-8")
def nettoyer(src_file, dest_file, delimiter, encoding):
    print(len(delimiter))
    with iterate_csv(src_file, encoding=encoding, delimiter=delimiter) as it:
        nettoyer_avec_spec(
            it,
            dest_file,
            spec,
        )


if __name__ == "__main__":
    nettoyer()
