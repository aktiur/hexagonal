import sys

import pandas as pd

from hexagonal.codes import normaliser_code_circonscription


def extraire_candidats(candidats, sensibilite_nfp, nuances_lfi, destination):
    candidats = pd.read_csv(candidats)
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
