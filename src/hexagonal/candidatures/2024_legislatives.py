import sys

import pandas as pd

from hexagonal.codes import normaliser_code_circonscription


RENOMMAGE = {
    "Code circonscription": "circonscription",
    "Numéro de panneau": "numero_panneau",
    "N° dépôt": "numero_depot",
    "Sexe du candidat": "sexe",
    "Nom du candidat": "nom",
    "Prénom du candidat": "prenom",
    "Date de naissance du candidat": "date_naissance",
    "Code nuance": "nuance",
    "Profession": "profession",
    "Sortant": "sortant",
    "Sexe remplaçant": "sexe_suppleant",
    "Nom remplaçant": "nom_suppleant",
    "Prénom remplaçant": "prenom_suppleant",
    "Date de naissance remplaçant": "date_naissance_suppleant",
    "Sortant remplaçant": "sortant_suppleant",
}


def extraire_candidats(candidats, sensibilite_nfp, nuances_lfi, destination):
    candidats = (
        pd.read_csv(candidats, delimiter=";")
        .rename(columns=RENOMMAGE)
        .reindex(columns=list(RENOMMAGE.values()))
    )
    candidats["circonscription"] = normaliser_code_circonscription(
        candidats["circonscription"]
    )
    candidats["sortant"] = candidats["sortant"] == "OUI"
    candidats["sortant_suppleant"] = candidats["sortant_suppleant"] == "OUI"
    candidats["profession"] = candidats["profession"].str.slice(1, 3)

    sensibilite_nfp = pd.read_csv(sensibilite_nfp)[
        ["circonscription", "numero_panneau", "sensibilite"]
    ]
    nuances_lfi = pd.read_csv(nuances_lfi)[
        ["circonscription", "numero_panneau", "nuance_lfi"]
    ]

    candidats = pd.merge(candidats, nuances_lfi, how="left")
    candidats = pd.merge(candidats, sensibilite_nfp, how="left")

    candidats.to_csv(destination, index=False)


def run():
    extraire_candidats(*sys.argv[1:])


if __name__ == "__main__":
    run()
