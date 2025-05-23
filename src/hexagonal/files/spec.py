import datetime
import tomllib
from enum import StrEnum
from pathlib import Path, PurePath
from typing import List, Optional, Union

import pandas as pd
from markupsafe import Markup
from pydantic import BaseModel

from hexagonal.files import ROOT_DIR
from hexagonal.utils import VRAI

SPEC = {}


def _load_spec():
    global SPEC

    with open(ROOT_DIR / "spec.toml", "rb") as fd:
        _spec = tomllib.load(fd)

    SPEC = {}
    for path, dataset_info in _spec.items():
        path = PurePath(path)

        SPEC[path] = Dataset.model_validate({"path": path, **dataset_info})


class DatasetType(StrEnum):
    SOURCE = "source"
    INTERMEDIAIRE = "intermediaire"
    CLEAN = "clean"
    MAIN = "main"


PRODUCTION_TYPES = [DatasetType.CLEAN, DatasetType.MAIN]


class ColonneType(StrEnum):
    STR = "str"
    DATE = "date"
    CODE_COMMUNE = "code_commune"
    CODE_DEPARTEMENT = "code_departement"
    CODE_REGION = "code_region"
    CODE_CIRCONSCRIPTION = "code_circonscription_legislative"
    INT = "entier"
    BOOL = "bool"
    QUALITATIVE = "qualitative"


PD_DTYPES = {
    ColonneType.STR: pd.StringDtype(),
    ColonneType.CODE_COMMUNE: pd.StringDtype(),
    ColonneType.CODE_DEPARTEMENT: pd.StringDtype(),
    ColonneType.CODE_REGION: pd.StringDtype(),
    ColonneType.INT: pd.Int64Dtype(),
    ColonneType.BOOL: pd.StringDtype(),
    ColonneType.QUALITATIVE: pd.CategoricalDtype(),
}


class Colonne(BaseModel):
    type: ColonneType
    description: str
    nullable: bool = False


class Dataset(BaseModel):
    path: PurePath
    nom: str
    type: DatasetType
    description: str
    url: str
    s3_url: str

    mimetype: str = ""

    # production
    section: Optional[str] = None

    # sources
    info_url: Optional[str] = None
    source_url: Optional[str] = None
    editeur: Optional[str] = None
    date: Optional[datetime.date] = None
    licence: Optional[str] = None

    # fichiers produits
    deps: Optional[List[PurePath]] = None

    # csv files
    colonnes: Optional[dict[str, Colonne]] = None

    def proprietes(self) -> dict[str, str]:
        props = {
            "Chemin interne": Markup(f"`{self.path}`"),
            "Format de fichier": self.mimetype,
            "URL de téléchargement": Markup(f"<{self.url}>"),
            "URL de téléchargement d'origine": self.source_url
            and Markup(f"<{self.source_url}>"),
            "URL d'information": self.info_url and Markup(f"<{self.info_url}>"),
            "Éditeur": self.editeur,
            "Date": self.date and self.date.strftime("%d/%m/%Y"),
            "Licence d'utilisation": self.licence,
        }

        return {k: v for k, v in props.items() if v}

    def sources(self):
        res = {}
        work = [*self.deps]
        while work:
            current = SPEC[work.pop()]
            if current.type == DatasetType.SOURCE:
                res[current.path] = current
            if current.deps:
                work.extend(current.deps)

        return [res[k] for k in sorted(res.keys())]

    def as_pandas_dataframe(self):
        if self.path.suffix == ".parquet":
            return pd.read_parquet(self.path)
        elif self.path.suffix == ".csv":
            params = {}
            for col_id, col_desc in self.colonnes.items():
                if col_desc.type in PD_DTYPES:
                    params.setdefault("dtype", {})[col_id] = PD_DTYPES[col_desc.type]

                if col_desc.type == ColonneType.DATE:
                    params.setdefault("parse_dates", []).append(col_id)
                    params.setdefault("date_format", "ISO8601")

            dataset = pd.read_csv(self.path, **params)

            for col_id, col_desc in self.colonnes.items():
                if col_desc.type == ColonneType.BOOL:
                    dataset[col_id] = dataset[col_id] == VRAI

            return dataset
        else:
            raise ValueError("Format impossible à convertir en dataframe")


def get_dataset(path: Union[str, bytes, Path]) -> Dataset:
    if isinstance(path, (str, bytes)):
        path = Path(path)

    path = path.resolve().relative_to(ROOT_DIR)
    return SPEC[path]


def get_dataframe(path: Union[str, bytes, Path]) -> pd.DataFrame:
    return get_dataset(path).as_pandas_dataframe()


_load_spec()
