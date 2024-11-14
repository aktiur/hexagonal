import csv
import json
import re
import sys
from operator import itemgetter
from zipfile import ZipFile, Path

from glom import glom, Coalesce, Invoke, T


PCS_FAM = {
    "Agriculteurs exploitants": "1",
    "Artisans, commerçants et chefs d'entreprise": "2",
    "Cadres et professions intellectuelles supérieures": "3",
    "Professions Intermédiaires": "4",
    "Employés": "5",
    "Ouvriers": "6",
    "Retraités": "7",
    "Autres personnes sans activité professionnelle": "8",
    "Sans profession déclarée": "",
}

PCS_CAT = {
    "Agriculteurs exploitants": "10",
    "Artisans": "21",
    "Commerçants et assimilés": "22",
    "Chefs d'entreprise de 10 salariés ou plus": "23",
    "Professions libérales et assimilés": "31",
    "Cadres de la fonction publique, professions intellectuelles et  artistiques": "32",
    "Cadres d'entreprise": "36",
    "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés": "41",
    "Professions intermédiaires administratives et commerciales des entreprises": "46",
    "Techniciens": "47",
    "Contremaîtres, agents de maîtrise": "48",
    "Employés de la fonction publique": "51",
    "Employés administratifs d'entreprise": "54",
    "Employés de commerce": "55",
    "Personnels des services directs aux particuliers": "56",
    "Ouvriers qualifiés": "61",
    "Ouvriers non qualifiés": "66",
    "Ouvriers agricoles": "69",
    "Anciens agriculteurs exploitants": "71",
    "Anciens artisans, commerçants, chefs d'entreprise": "72",
    "Anciens cadres et professions intermédiaires": "73",
    "Anciens employés et ouvriers": "76",
    "Chômeurs n'ayant jamais travaillé": "81",
    "Inactifs divers (autres que retraités)": "82",
    "Sans profession déclarée": "",
}


def possiblement_nul(d):
    if isinstance(d, dict):
        if "@xsi:nil" in d and d["@xsi:nil"] == "true":
            return ""
        raise ValueError(f"Valeur incorrecte: {d!r}")
    return d


def legislatures_depute(depute):
    if not isinstance((mandats := depute["mandats"]["mandat"]), list):
        mandats = [mandats]
    return sorted(
        set(str(m["legislature"]) for m in mandats if m["typeOrgane"] == "ASSEMBLEE")
    )


spec_extraction_liste_deputee = {
    "identifiant_an": Coalesce("uid.#text", "uid"),
    "civilite": "etatCivil.ident.civ",
    "prenom": "etatCivil.ident.prenom",
    "nom": "etatCivil.ident.nom",
    "date_naissance": ("etatCivil.infoNaissance.dateNais", possiblement_nul),
    "ville_naissance": ("etatCivil.infoNaissance.villeNais", possiblement_nul),
    "departement_naissance": ("etatCivil.infoNaissance.depNais", possiblement_nul),
    "legislatures": (legislatures_depute, "/".join),
    "profession": ("profession.libelleCourant", possiblement_nul),
    "csp_agregee": (
        "profession.socProcINSEE.famSocPro",
        possiblement_nul,
        Invoke(PCS_FAM.get).specs(T).constants(""),
    ),
    "csp": (
        "profession.socProcINSEE.catSocPro",
        possiblement_nul,
        Invoke(PCS_CAT.get).specs(T).constants(""),
    ),
}


def json_deputees(archive):
    for deputee_file in (Path(archive) / "json" / "acteur").iterdir():
        with deputee_file.open() as fd:
            yield json.load(fd)["acteur"]


def extraire_liste_deputes(archive, out_file):
    writer = csv.DictWriter(out_file, fieldnames=list(spec_extraction_liste_deputee))

    writer.writeheader()

    deputes = glom(json_deputees(archive), [spec_extraction_liste_deputee])

    # noinspection PyTypeChecker
    writer.writerows(sorted(deputes, key=itemgetter("identifiant_an")))


def run():
    archive_path, out_path = sys.argv[1:]

    with ZipFile(archive_path) as archive, open(out_path, "w") as out_file:
        extraire_liste_deputes(archive, out_file)


if __name__ == "__main__":
    run()
