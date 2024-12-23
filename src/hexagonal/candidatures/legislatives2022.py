import re
import sys

import pandas as pd

from hexagonal.codes import normaliser_code_circonscription


COLONNES_LEMONDE = {
    "Département": "departement",
    "Numéro Circonscription": "circonscription",
    "Numéro Panneau": "numero_panneau",
    "Nom": "nom_lemonde",
    "Nuance agrégée par Le Monde": "nuance_lemonde",
    "Parti agrégé par Le Monde": "parti_lemonde",
}

COLONNES_LEGIS_2022 = {
    "DEP": "departement",
    "panneau": "numero_panneau",
    "NCIRCO": "circonscription",
    "CODAGE_LEGIS2022": "nuance_legis_2022",
    "CODAGE_NUPES_ENSEMBLE_OUTREMER": "regroupement_om_legis_2022",
}


def extraire_candidats(candidats, nuances_lemonde, nuances_legis_2022, destination):
    tour = re.search(r"2022-legislatives-(\d)-candidats.csv", candidats).group(1)
    candidats = pd.read_csv(candidats, dtype=str)

    if tour == "1":
        # deux candidats de la 92-11 sont inversés dans le fichier du ministère, LÉVÊQUE et ROLLOT
        candidats.loc[5407:5408, "numero_panneau"] = ["9", "8"]

    del candidats["departement"]

    nuances_lemonde = pd.read_csv(
        nuances_lemonde,
        usecols=list(COLONNES_LEMONDE),
        dtype=str,
    ).rename(columns=COLONNES_LEMONDE)
    nuances_lemonde["circonscription"] = normaliser_code_circonscription(
        nuances_lemonde["departement"].str.lstrip("0")
        + nuances_lemonde["circonscription"].str.zfill(2)
    )
    del nuances_lemonde["departement"]

    nuances_legis_2022 = pd.read_csv(
        nuances_legis_2022,
        usecols=list(COLONNES_LEGIS_2022),
        dtype=str,
    ).rename(columns=COLONNES_LEGIS_2022)
    nuances_legis_2022["circonscription"] = normaliser_code_circonscription(
        nuances_legis_2022["departement"]
        + nuances_legis_2022["circonscription"].str.zfill(2)
    )
    del nuances_legis_2022["departement"]

    candidats = pd.merge(candidats, nuances_lemonde, how="left")
    candidats = pd.merge(candidats, nuances_legis_2022, how="left")

    candidats["nom"] = candidats["nom_lemonde"]
    del candidats["nom_lemonde"]

    candidats.to_csv(destination, index=False)


def run():
    extraire_candidats(*sys.argv[1:])


if __name__ == "__main__":
    run()
