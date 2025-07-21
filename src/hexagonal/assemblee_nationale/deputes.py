from pathlib import Path

import click
import pandas as pd

CHAMPS_MANDAT = [
    "id_mandat",
    "circonscription",
    "suppleante",
    "date_debut",
    "cause_debut_mandat",
    "place",
]
CHAMPS_COMMISSION = [
    "id_commission",
    "commission",
    "date_debut_commission",
    "poste_commission",
]
CHAMPS_GROUPE = ["id_groupe", "abreviation_groupe", "date_debut_groupe", "poste_groupe"]


def garder_entree_principale(entrees):
    return pd.concat(
        [
            entrees[entrees["qualite"] != "Membre"],
            entrees[entrees["qualite"] == "Membre"],
        ]
    ).drop_duplicates("id_personne", keep="first")


def creer_liste(fiches, mandats, commissions, affiliations, adresses_electroniques):
    fiches = pd.read_csv(fiches).set_index("id_personne")
    mandats = pd.read_csv(mandats)
    commissions = pd.read_csv(commissions)
    affiliations = pd.read_csv(affiliations)
    adresses_electroniques = pd.read_csv(adresses_electroniques)

    mandats_actifs = mandats[mandats["date_fin"].isna()].set_index("id_personne")
    assert mandats_actifs.index.is_unique

    commissions_actuelles = (
        garder_entree_principale(commissions[commissions["date_fin"].isna()])
        .set_index("id_personne")
        .rename(
            columns={
                "qualite": "poste_commission",
                "date_debut": "date_debut_commission",
            }
        )
    )

    affiliations_actuelles = (
        garder_entree_principale(affiliations[affiliations["date_fin"].isna()])
        .set_index("id_personne")
        .rename(columns={"qualite": "poste_groupe", "date_debut": "date_debut_groupe"})
    )

    emails = adresses_electroniques[adresses_electroniques["type"] == "email"]
    est_email_assemblee = emails["adresse"].str.endswith("@assemblee-nationale.fr")

    emails_assemblee = (
        emails[est_email_assemblee]
        .drop_duplicates("id_personne")
        .set_index("id_personne")
    )["adresse"]

    autres_emails = (
        emails[~est_email_assemblee]
        .drop_duplicates("id_personne")
        .set_index("id_personne")
    )["adresse"]

    telephone_assemblee = (
        adresses_electroniques[
            (adresses_electroniques["type"] == "telephone")
            & (adresses_electroniques["poids"] == 1.0)
        ]
        .drop_duplicates("id_personne")
        .set_index("id_personne")["adresse"]
    )

    telephone_circonscription = (
        adresses_electroniques[
            (adresses_electroniques["type"] == "telephone")
            & (adresses_electroniques["poids"] == 22.0)
        ]
        .drop_duplicates("id_personne")
        .set_index("id_personne")["adresse"]
    )

    deputes = fiches.join(
        mandats_actifs[CHAMPS_MANDAT],
        how="inner",
    )
    deputes = deputes.join(
        commissions_actuelles[CHAMPS_COMMISSION],
    )
    deputes = deputes.join(
        affiliations_actuelles[CHAMPS_GROUPE],
    )
    deputes["email_an"] = deputes.index.map(emails_assemblee)
    deputes["email_autre"] = deputes.index.map(autres_emails)
    deputes["telephone_an"] = deputes.index.map(telephone_assemblee)
    deputes["telephone_circonscription"] = deputes.index.map(telephone_circonscription)

    return deputes


@click.command()
@click.argument(
    "dossier",
    type=click.Path(exists=True, readable=True, dir_okay=True, path_type=Path),
    required=True,
)
@click.argument(
    "destination",
    type=click.Path(writable=True, dir_okay=False, path_type=Path),
    required=True,
)
def run(dossier, destination):
    deputes = creer_liste(
        fiches=dossier / "fiches.csv",
        mandats=dossier / "mandats.csv",
        commissions=dossier / "commissions.csv",
        affiliations=dossier / "affiliations.csv",
        adresses_electroniques=dossier / "adresses_electroniques.csv",
    )

    destination.parent.mkdir(parents=True, exist_ok=True)
    deputes.to_csv(destination)


if __name__ == "__main__":
    run()
