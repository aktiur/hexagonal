import enum
from dataclasses import dataclass


@dataclass
class TypeNom:
    code: int
    article: str
    charniere: str


TYPES_NOMS = [
    TypeNom(0, "", "de "),
    TypeNom(1, "", "d'"),
    TypeNom(2, "le ", "du "),
    TypeNom(3, "la ", "de la "),
    TypeNom(4, "les ", "des "),
    TypeNom(5, "l'", "de l'"),
    TypeNom(6, "aux ", "des "),
    TypeNom(7, "las ", "de las "),
    TypeNom(8, "los ", "de los"),
]
