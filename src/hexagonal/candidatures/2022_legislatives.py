import re
import sys

import pandas as pd

from hexagonal.codes import normaliser_code_circonscription

COLONNES_CANDIDATS = {
    "Code du département": "departement",
    "Code circonscription": "circonscription",
    "N° panneau": "numero_panneau",
    "N° candidat": "numero_depot",
    "Sexe candidat": "sexe",
    "Nom candidat": "nom",
    "Prénom candidat": "prenom",
    "Date naissance candidat": "date_naissance",
    "Nuance candidat": "nuance",
    "Profession candidat": "profession",
    "Le candidat est sortant": "sortant",
    "Sexe remplaçant": "sexe_suppleant",
    "Nom remplaçant": "nom_suppleant",
    "Prénom remplaçant": "prenom_suppleant",
    "Date naiss. remplaçant": "date_naissance_suppleant",
    "Le remplaçant est sortant": "sortant_suppleant",
}

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
    candidats = (
        pd.read_csv(
            candidats,
            delimiter="\t",
            encoding="latin1",
            dtype=str,
            usecols=list(COLONNES_CANDIDATS),
        )
        .rename(columns=COLONNES_CANDIDATS)
        .reindex(columns=list(COLONNES_CANDIDATS.values()))
    )

    if tour == "1":
        # deux candidats de la 92-11 sont inversés dans le fichier du ministère, LÉVÊQUE et ROLLOT
        candidats.loc[5407:5408, "numero_panneau"] = ["9", "8"]

    candidats["circonscription"] = normaliser_code_circonscription(
        candidats["departement"] + candidats["circonscription"]
    )
    del candidats["departement"]

    for c in ["date_naissance", "date_naissance_suppleant"]:
        candidats[c] = pd.to_datetime(candidats[c], format="%d/%m/%Y").dt.strftime(
            "%Y-%m-%d"
        )

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

    candidats.to_csv(destination, index=False)


def run():
    extraire_candidats(*sys.argv[1:])


if __name__ == "__main__":
    run()
