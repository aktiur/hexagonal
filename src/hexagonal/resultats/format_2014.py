import sys
from itertools import chain
from typing import Literal

import pandas as pd

partie_commune = [
    "numero_tour",  # -- Champ 1  : N° tour
    "departement",  # -- Champ 2  : Code département
    "commune",  # -- Champ 3  : Code commune
    "nom_commune",
    "circonscription",
    "canton",
]

partie_bureau = [
    "bureau",  # -- Champ 5  : N° de bureau de vote
    "inscrits",  # -- Champ 6  : Inscrits
    "votants",  # -- Champ 7  : Votants
    "exprimes",  # -- Champ 8  : Exprimés
    "numero_panneau",  # -- Champ 9  : N° de dépôt de la liste
    "nom",  # -- Champ 10 : Nom du candidat tête de liste
    "prenom",  # -- Champ 11 : Prénom du candidat  tête de liste
    "nuance",  # -- Champ 12 : Code nuance de la liste
    "voix",  # -- Champ 13 : Nombre de voix
]


transforms: dict[str, Literal["int", "category"]] = {
    "circonscription": "int",
    "numero_tour": "int",
    "numero_panneau": "int",
    "nuance": "category",
    "inscrits": "int",
    "votants": "int",
    "exprimes": "int",
    "voix": "int",
}

population = [
    "circonscription",
    "numero_tour",
    "canton",
    "inscrits",
    "votants",
    "exprimes",
]
par_candidat = ["numero_panneau", "nom", "prenom", "nuance", "voix"]


types_par_colonne = {
    **{h: str for h in chain(partie_commune, partie_bureau)},
    **{"inscrits": int, "votants": int, "exprimes": int, "voix": int},
}


def clean_results(
    src,
    dest,
    delimiter=";",
    encoding="latin1",
):
    # trouver la première ligne
    with open(src, "r", encoding=encoding) as f:
        for numero_ligne, ligne in enumerate(f):  # noqa: B007
            if delimiter in ligne:
                nb_champs = len(ligne.split(delimiter))
                break
        else:
            raise ValueError("Impossible de trouver la première ligne")

    nb_communs = nb_champs - len(partie_bureau)
    names = partie_commune[:nb_communs] + partie_bureau

    resultats: pd.DataFrame = pd.read_csv(
        src,
        sep=delimiter,
        skiprows=numero_ligne,
        names=names,
        header=None,
        dtype=types_par_colonne,  # type: ignore
        encoding=encoding,
    )

    for field, transform in transforms.items():
        if field in resultats.columns:
            resultats[field] = resultats[field].astype(transform)

    if resultats.nom.nunique() < 1000:
        resultats["nom"] = resultats["nom"].astype("category")
        resultats["prenom"] = resultats["prenom"].astype("category")

    resultats["bureau_de_vote"] = (
        resultats["departement"].str.zfill(2)
        + resultats["commune"].str.zfill(3)
        + "-"
        + resultats["bureau"].str.zfill(4)
    )

    if "circonscription" in resultats.columns:
        resultats["circonscription"] = (
            resultats["circonscription"].astype(str).str.zfill(4)
        )

    clean_columns = [
        "bureau_de_vote",
        *(c for c in (population + par_candidat) if c in resultats.columns),
    ]
    df_clean = resultats.loc[:, clean_columns].reset_index(drop=True)
    df_clean.to_csv(f"{dest}", index=False)


def run():
    src, dest, encoding, delimiter = sys.argv[1:]
    clean_results(src, dest, delimiter=delimiter, encoding=encoding)


if __name__ == "__main__":
    run()
