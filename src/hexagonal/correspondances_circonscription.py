import pandas as pd

from hexagonal.codes import normaliser_code_circonscription


def etablir_correspondances(resultats_bdv, candidats_t1, destination):
    resultats = pd.read_csv(
        resultats_bdv,
        usecols=["bureau_de_vote", "numero_panneau", "nom", "prenom"],
    )
    candidats = pd.read_csv(candidats_t1, sep=";").rename(
        columns={
            "Nom du candidat": "nom",
            "Prénom du candidat": "prenom",
            "Numéro de panneau": "numero_panneau",
            "Code circonscription": "circonscription",
        }
    )
    candidats["circonscription"] = normaliser_code_circonscription(
        candidats["circonscription"]
    )

    correspondance = pd.merge(
        resultats,
        candidats,
    )
