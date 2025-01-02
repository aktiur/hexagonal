from pathlib import PurePath

import pytest

from hexagonal.files.spec import PRODUCTION_TYPES, SPEC

CSV_PRODUCTIONS = [
    str(k)
    for k, info in SPEC.items()
    if info.mimetype == "text/csv" and info.type in PRODUCTION_TYPES
]


@pytest.fixture(scope="session", params=CSV_PRODUCTIONS)
def csv_path(request):
    return request.param


@pytest.fixture(scope="session")
def file_info(csv_path):
    return SPEC[PurePath(csv_path)]


@pytest.fixture(scope="session")
def csv_dataset(file_info):
    return file_info.as_pandas_dataframe()


def test_pas_de_colonne_vide_dans_les_fichiers_propres(csv_dataset):
    colonne_est_vide = csv_dataset.isnull().all(axis=0)
    colonnes_vides = list(colonne_est_vide.loc[colonne_est_vide].index)
    assert colonnes_vides == []


def test_colonnes_non_nullables(csv_dataset, file_info):
    non_nullables = [c for c, i in file_info.colonnes.items() if not i.nullable]

    valeurs_nulles = csv_dataset[non_nullables].isnull().any(axis=0)
    colonnes_valeurs_vides = list(valeurs_nulles.loc[valeurs_nulles].index)
    assert colonnes_valeurs_vides == []
