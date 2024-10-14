import sys

import pandas as pd


def etablir_correspondances(resultats, candidats, destination):
    resultats = pd.read_csv(
        resultats,
        usecols=["bureau_de_vote", "numero_panneau", "nom", "prenom"],
        dtype=str,
    )
    candidats = pd.read_csv(
        candidats,
        usecols=["circonscription", "numero_panneau", "nom", "prenom"],
        dtype=str,
    )

    correspondance = pd.merge(
        resultats,
        candidats,
    )[["bureau_de_vote", "circonscription"]].drop_duplicates()

    assert correspondance.duplicated(["bureau_de_vote"], keep=False).sum() == 0

    correspondance.to_csv(destination, index=False)


def run():
    etablir_correspondances(*sys.argv[1:])


if __name__ == "__main__":
    run()
