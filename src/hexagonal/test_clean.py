from pathlib import Path

import pandas as pd
import pytest

DATA_DIR = Path("data")
CLEAN_DIR = DATA_DIR / "02_clean"

CLEAN_CSV_FILES = [
    str(
        dirpath / filename
    )  # str pour que le path s'affiche dans le rapport d'erreur de pytest
    for dirpath, _, filenames in CLEAN_DIR.walk()
    for filename in filenames
    if filename.endswith(".csv")
]


@pytest.fixture(scope="module", params=CLEAN_CSV_FILES)
def clean_csv(request):
    df = pd.read_csv(request.param, encoding="utf-8", sep=",", dtype=str)

    return df


def test_pas_de_colonne_vide(clean_csv):
    colonne_est_vide = clean_csv.isnull().all(axis=0)
    colonnes_vides = list(colonne_est_vide.loc[colonne_est_vide].index)
    assert colonnes_vides == []
