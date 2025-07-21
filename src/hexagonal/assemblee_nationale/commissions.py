import sys
from operator import itemgetter
from zipfile import ZipFile

from glom import Coalesce, Flatten, Iter, S, Spec, glom

from hexagonal.assemblee_nationale.utils import (
    ecrire_csv,
    json_organes,
    json_personnes,
    possiblement_nul,
    to_list,
)


def est_une_commission(g):
    return g["codeType"] == "COMPER"


def est_participation_commission(g):
    return g["typeOrgane"] == "COMPER"


def liste_commissions(archive):
    spec_extraction_commission = {
        "id": "uid",
        "nom": "libelle",
        "nom_abrege": "libelleAbrege",
        "date_debut": "viMoDe.dateDebut",
        "date_fin": "viMoDe.dateFin",
    }

    return sorted(
        glom(
            json_organes(archive),
            Iter().filter(est_une_commission).map(spec_extraction_commission),
        ),
        key=itemgetter("id"),
    )


def liste_participations(archive, com_map):
    spec_extraction_affiliation = {
        "id_personne": S.uid,
        "id_commission": "organes.organeRef",
        "prenom": S.prenom,
        "nom": S.nom,
        "commission": ("organes.organeRef", com_map.get),
        "legislature": "legislature",
        "date_debut": "dateDebut",
        "date_fin": ("dateFin", possiblement_nul),
        "qualite": "infosQualite.codeQualite",
    }

    spec_deputees = (
        S(
            uid=Spec(Coalesce("uid.#text", "uid")),
            nom=Spec("etatCivil.ident.nom"),
            prenom=Spec("etatCivil.ident.prenom"),
        ),  # enregistre prenom et nom dans le scope
        "mandats.mandat",  # selectionne les mandats
        to_list,  # convertit en une liste pour les quelques cas de mandats uniques
        Iter().filter(est_participation_commission).map(spec_extraction_affiliation),
    )

    return sorted(
        glom(
            json_personnes(archive),
            (Iter(spec_deputees), Flatten()),
        ),
        key=itemgetter("date_debut", "id_personne"),
    )


def extraire_groupes_et_affilations(archive, participations_path):
    commissions = liste_commissions(archive)
    abrege_coms = {g["id"]: g["nom_abrege"] for g in commissions}
    participations = liste_participations(archive, abrege_coms)
    ecrire_csv(participations, list(participations[0]), participations_path)


def run():
    archive_path, participations_path = sys.argv[1:]

    with ZipFile(archive_path) as archive:
        extraire_groupes_et_affilations(archive, participations_path)


if __name__ == "__main__":
    run()
