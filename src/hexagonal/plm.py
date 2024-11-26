from dataclasses import dataclass
from typing import List


@dataclass
class SecteurPLM:
    numero: int
    arrondissement: List[int]


@dataclass
class CommunePLM:
    nom: str
    code: str
    format_arrondissement: str
    nb_arrondissements: int
    secteurs: List[SecteurPLM]

    def __post_init__(self):
        self._secteur_par_arrondissement = {
            arr: sec for sec in self.secteurs for arr in sec.arrondissement
        }

    def bureau_vers_secteur(self, bureau):
        assert bureau.startswith(self.code)
        id_bureau = bureau[6:]
        arrondissement = int(id_bureau[:2])
        return f"{self.code}SR{self._secteur_par_arrondissement[arrondissement].numero:02d}"

    def bureau_vers_arrondissement(self, bureau):
        assert bureau.startswith(self.code)
        id_bureau = bureau[6:]
        arrondissement = int(id_bureau[:2])

        return self.format_arrondissement.format(arrondissement)


PARIS = CommunePLM(
    nom="Paris",
    code="75056",
    format_arrondissement="751{:02d}",
    nb_arrondissements=20,
    secteurs=[
        SecteurPLM(1, [1, 2, 3, 4]),
        *[SecteurPLM(i, [i]) for i in range(5, 21)],
    ],
)

LYON = CommunePLM(
    nom="Lyon",
    code="69123",
    format_arrondissement="6938{:01d}",
    nb_arrondissements=9,
    secteurs=[SecteurPLM(i, [i]) for i in range(1, 10)],
)

MARSEILLE = CommunePLM(
    nom="Marseille",
    code="13055",
    format_arrondissement="132{:02d}",
    nb_arrondissements=16,
    secteurs=[
        SecteurPLM(1, [1, 7]),
        SecteurPLM(2, [2, 3]),
        SecteurPLM(3, [4, 5]),
        SecteurPLM(4, [6, 8]),
        SecteurPLM(5, [9, 10]),
        SecteurPLM(6, [11, 12]),
        SecteurPLM(7, [13, 14]),
        SecteurPLM(8, [15, 16]),
    ],
)

PLM = [
    PARIS,
    LYON,
    MARSEILLE,
]


def code_bureaux_vers_secteur(s_bureaux):
    code_commune = s_bureaux.str.slice(0, 5)

    for c in PLM:
        selection_bureaux = code_commune == c.code
        code_commune.loc[selection_bureaux] = s_bureaux.loc[selection_bureaux].map(
            c.bureau_vers_secteur
        )

    return code_commune


def code_bureaux_vers_arrondissement(s_bureaux):
    code_commune = s_bureaux.str.slice(0, 5)

    for c in PLM:
        selection_bureaux = code_commune == c.code
        code_commune[selection_bureaux] = s_bureaux.loc[selection_bureaux].map(
            c.bureau_vers_arrondissement
        )

    return code_commune
