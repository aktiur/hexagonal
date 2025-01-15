import csv
from operator import itemgetter
from zipfile import ZipFile

import click
from glom import Coalesce, Invoke, T, glom

from hexagonal.assemblee_nationale.utils import (
    json_personnes,
    possiblement_nul,
    to_list,
)

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
    "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés": "41",  # noqa: E501
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


def legislatures_depute(depute):
    if not isinstance((mandats := depute["mandats"]["mandat"]), list):
        mandats = [mandats]
    return sorted(
        set(str(m["legislature"]) for m in mandats if m["typeOrgane"] == "ASSEMBLEE")
    )


TYPES_ADRESSES = {
    0: "adresse_officielle",
    1: "adresse_parisienne",
    2: "adresse_circonscription",
    3: "telephone_presse",
    11: "telephone",
    12: "fax",
    15: "email",
    22: "site_web",
    23: "url_senateur",
    24: "twitter",
    25: "facebook",
    29: "instagram",
    30: "linkedin",
}


spec_extraction_liste_deputee = {
    "id_personne": Coalesce("uid.#text", "uid"),
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


spec_adresse_postale = {
    "id_adresse": Coalesce("uid.#text", "uid"),
    "id_personne": Coalesce("id_personne.#text", "id_personne"),
    "type": ("type", int, TYPES_ADRESSES.get),
    "intitule": Coalesce("intitule", default=""),
    "numero_rue": Coalesce("numeroRue", default=""),
    "code_postal": Coalesce("codePostal", default=""),
    "ville": Coalesce("ville", default=""),
    "complement": Coalesce("complementAdresse", default=""),
    "nom_rue": Coalesce("nomRue", default=""),
    "poids": Coalesce("poids", default=""),
}

spec_adresse_electronique = {
    "id_adresse": Coalesce("uid.#text", "uid"),
    "id_personne": Coalesce("id_personne.#text", "id_personne"),
    "type": ("type", int, TYPES_ADRESSES.get),
    "adresse_rattachement": Coalesce("adresseDeRattachement", default=""),
    "adresse": Coalesce("valElec", default=""),
    "poids": Coalesce("poids", default=""),
}


def extraire_liste_deputes(
    archive, fiches, deputes, adresses_postales, adresses_electroniques
):
    personnes = sorted(
        glom(json_personnes(archive), [spec_extraction_liste_deputee]),
        key=itemgetter("id_personne"),
    )

    liste_adresses = [
        {"id_personne": d["uid"], **a}
        for d in json_personnes(archive)
        if "@xsi:nil" not in d["adresses"]
        for a in to_list(d["adresses"]["adresse"])
    ]

    liste_adresses_postales = glom(
        [a for a in liste_adresses if int(a["type"]) <= 10],
        [spec_adresse_postale],
    )
    liste_adresses_electroniques = glom(
        [a for a in liste_adresses if int(a["type"]) > 10],
        [spec_adresse_electronique],
    )

    fiches_writer = csv.DictWriter(
        fiches, fieldnames=list(spec_extraction_liste_deputee)
    )
    fiches_writer.writeheader()
    fiches_writer.writerows(personnes)

    deputes_writer = csv.DictWriter(
        deputes, fieldnames=list(spec_extraction_liste_deputee)
    )
    deputes_writer.writeheader()
    deputes_writer.writerows(p for p in personnes if p["legislatures"])

    adresses_postales_writer = csv.DictWriter(
        adresses_postales, fieldnames=list(spec_adresse_postale)
    )
    adresses_postales_writer.writeheader()
    adresses_postales_writer.writerows(liste_adresses_postales)

    adresses_electroniques_writer = csv.DictWriter(
        adresses_electroniques, fieldnames=list(spec_adresse_electronique)
    )
    adresses_electroniques_writer.writeheader()
    adresses_electroniques_writer.writerows(liste_adresses_electroniques)


@click.command()
@click.argument(
    "archive_path", type=click.Path(exists=True, file_okay=True, readable=True)
)
@click.argument("fiches", type=click.File("w"))
@click.argument("deputes", type=click.File("w"))
@click.argument("adresses_postales", type=click.File("w"))
@click.argument("adresses_electroniques", type=click.File("w"))
def run(archive_path, fiches, deputes, adresses_postales, adresses_electroniques):
    with ZipFile(archive_path) as archive:
        extraire_liste_deputes(
            archive, fiches, deputes, adresses_postales, adresses_electroniques
        )


if __name__ == "__main__":
    run()
