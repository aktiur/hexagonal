import sys
from operator import itemgetter
from zipfile import ZipFile

from glom import S, Flatten, glom, Iter, Coalesce, Spec

from hexagonal.assemblee_nationale.utils import (
    possiblement_nul,
    json_organes,
    ecrire_csv,
    json_deputees,
    to_list,
)


def est_un_groupe(g):
    return g["codeType"] == "GP" and g["libelleAbrege"] != "NI"


def est_une_affiliation(g):
    return (
        g["typeOrgane"] == "GP"
        and g["infosQualite"]["codeQualite"] != "Député non-inscrit"
    )


def liste_groupes(archive):
    spec_extraction_groupe = {
        "id_groupe": "uid",
        "legislature": ("legislature", int),
        "nom": "libelle",
        "abrege": "libelleAbrege",
        "abreviation": "libelleAbrev",
        "date_debut": "viMoDe.dateDebut",
        "date_fin": "viMoDe.dateFin",
        "position": "positionPolitique",
        "preseance": ("preseance", int),
    }

    return sorted(
        glom(
            json_organes(archive),
            Iter().filter(est_un_groupe).map(spec_extraction_groupe),
        ),
        key=itemgetter("date_debut", "id_groupe"),
    )


def liste_affiliations(archive, groupe_map):
    spec_extraction_affiliation = {
        "id_personne": S.uid,
        "id_groupe": "organes.organeRef",
        "prenom": S.prenom,
        "nom": S.nom,
        "abreviation_groupe": ("organes.organeRef", groupe_map.get),
        "legislature": "legislature",
        "suppleante": Coalesce("suppleants.suppleant.suppleantRef", default=""),
        "date_debut": "dateDebut",
        "date_fin": ("dateFin", possiblement_nul),
    }

    spec_deputees = (
        S(
            uid=Spec(Coalesce("uid.#text", "uid")),
            nom=Spec("etatCivil.ident.nom"),
            prenom=Spec("etatCivil.ident.prenom"),
        ),  # enregistre prenom et nom dans le scope
        "mandats.mandat",  # selectionne les mandats
        to_list,  # convertit en une liste pour les quelques cas de mandats uniques
        Iter().filter(est_une_affiliation).map(spec_extraction_affiliation),
    )

    return sorted(
        glom(
            json_deputees(archive),
            (Iter(spec_deputees), Flatten()),
        ),
        key=itemgetter("date_debut", "id_personne"),
    )


def extraire_groupes_et_affilations(archive, groupes_path, affiliations_path):
    groupes = liste_groupes(archive)
    ecrire_csv(groupes, list(groupes[0]), groupes_path)
    abrev_groupes = {g["id_groupe"]: g["abreviation"] for g in groupes}
    affiliations = liste_affiliations(archive, abrev_groupes)
    ecrire_csv(affiliations, list(affiliations[0]), affiliations_path)


def run():
    archive_path, groupes_path, affilations_path = sys.argv[1:]

    with ZipFile(archive_path) as archive:
        extraire_groupes_et_affilations(archive, groupes_path, affilations_path)


if __name__ == "__main__":
    run()
