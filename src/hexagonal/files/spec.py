import datetime
import tomllib
from enum import StrEnum
from operator import attrgetter
from pathlib import Path

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from hexagonal.files import ROOT_DIR, get_main_dir
from hexagonal.files.dvc_files import DVCFile
from hexagonal.utils import VRAI

props_funcs = {
    "date": lambda d: d.strftime("%d/%m/%Y"),
}


class DatasetType(StrEnum):
    SOURCE = "source"
    INTERMEDIAIRE = "intermediaire"
    CLEAN = "clean"
    MAIN = "main"


PRODUCTION_TYPES = [DatasetType.CLEAN, DatasetType.MAIN]


class ColonneType(StrEnum):
    STR = "str"
    DATE = "date"
    CODE_IRIS = "code_iris"
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


class ColonneMetadata(BaseModel):
    type: ColonneType
    description: str | None = None
    nullable: bool = False


class DatasetSpec(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=False, serialize_by_alias=False
    )

    path: Path = Field(alias="Chemin interne")
    nom: str
    description: str

    mimetype: str | None = Field(alias="Format de fichier", default=None)

    def props(self):
        props = {}
        for name, field in self.model_fields.items():
            if field.alias and getattr(self, name):
                if name in props_funcs:
                    props[field.alias] = props_funcs[name](getattr(self, name))
                else:
                    props[field.alias] = getattr(self, name)
        return props

    def as_pandas_dataframe(self):
        if self.mimetype == "application/vnd.apache.parquet":
            return pd.read_parquet(self.path)
        elif self.mimetype == "text/csv":
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


class SourceSpec(DatasetSpec):
    # sources
    info_url: str | None = Field(alias="URL d'information", default=None)
    editeur: str | None = Field(alias="Éditeur", default=None)
    date: datetime.date | None = Field(alias="Date", default=None)
    licence: str | None = Field(alias="Licence d'utilisation", default=None)


class ProductionSpec(DatasetSpec):
    section: str | None = Field(default=None)

    # csv files
    colonnes: dict[str, ColonneMetadata] | None = None


def load_spec(path: Path) -> DatasetSpec:
    toml_path = path.with_suffix(f"{path.suffix}.toml")
    if not toml_path.is_file():
        raise FileNotFoundError(
            f"Le fichier {path} n'est pas un dataset (fichier toml manquant)."
        )

    with toml_path.open("rb") as fd:
        spec = tomllib.load(fd)

    if get_main_dir(path) == "01_raw":
        return SourceSpec.model_validate({"path": path, **spec})
    return ProductionSpec.model_validate({"path": path, **spec})


class Dataset:
    def __init__(self, path, spec: DatasetSpec = None, dvc_file: DVCFile = None):
        self.path = path
        if not spec:
            spec = load_spec(path)
        self.spec = spec
        self.dvc_file = dvc_file


def load_all_specs():
    specs = []

    roots = [
        ("01_raw", SourceSpec),
        ("02_clean", ProductionSpec),
        ("03_main", ProductionSpec),
    ]

    for data_root, klass in roots:
        for d, _, files in (ROOT_DIR / "data" / data_root).walk():
            for f in files:
                path = d / f
                if path.suffix == ".toml":
                    with path.open("rb") as fd:
                        spec = tomllib.load(fd)

                    dataset_path = path.with_suffix("").resolve().relative_to(ROOT_DIR)
                    specs.append(klass.model_validate({"path": dataset_path, **spec}))

    specs = {spec.path: spec for spec in sorted(specs, key=attrgetter("path"))}

    return specs


def get_dataframe(path: str | bytes | Path) -> pd.DataFrame:
    if isinstance(path, str | bytes):
        path = Path(path)
    return load_spec(path).as_pandas_dataframe()
