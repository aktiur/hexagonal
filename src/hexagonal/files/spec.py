import datetime
import tomllib
from enum import StrEnum
from pathlib import PurePath
from typing import Optional, List

from markupsafe import Markup
from pydantic import BaseModel

from hexagonal.files import ROOT_DIR


SPEC = {}


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
    INT = "int"


class Colonne(BaseModel):
    nom: str
    type: ColonneType
    description: str


class Dataset(BaseModel):
    path: PurePath
    nom: str
    type: DatasetType
    description: str
    url: str
    s3_url: str

    mimetype: str = ""

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


with open(ROOT_DIR / "spec.toml", "rb") as fd:
    _spec = tomllib.load(fd)

    for path, dataset_info in _spec.items():
        path = PurePath(path)

        SPEC[path] = Dataset(path=path, **dataset_info)
