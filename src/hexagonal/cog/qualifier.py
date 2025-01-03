from hexagonal.cog.type_nom import TYPES_NOMS


def article(entite):
    return TYPES_NOMS[int(entite["TNCC"])].article


def charniere(entite):
    return TYPES_NOMS[int(entite["TNCC"])].charniere
