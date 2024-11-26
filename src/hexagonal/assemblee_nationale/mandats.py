import csv
import sys
from operator import itemgetter
from zipfile import ZipFile

from glom import S, Flatten, glom, Iter, Check, SKIP, Spec, Coalesce

from hexagonal.assemblee_nationale.utils import json_deputees, possiblement_nul, to_list

CAUSES_MANDATS = {
    "élections générales": "GENERAL",
    "remplacement d'un député ayant démissionné pour cause d’incompatibilité prévue aux articles LO 137, LO 137-1, LO 141 ou LO 141-1 du code électoral": "DEM-INCOMPAT",
    "remplacement d'un député décédé": "DCD",
    "remplacement d'un député en mission au-delà de 6 mois": "MISSION",
    "remplacement d'un député nommé au Conseil Constitutionnel": "DEM-CC",
    "remplacement d'un député nommé au Gouvernement": "GOUV-ENTREE",
    "reprise de l'exercice du mandat d'un ancien membre du Gouvernement": "GOUV-RETOUR",
    "élection partielle": "PARTIELLE",
    "élection partielle, en remplacement d'un député décédé et sans suppléant": "PARTIELLE-DCD",
    "élection partielle, remplacement d'un député déchu de son mandat": "PARTIELLE-DECHEANCE",
    "élection partielle, remplacement d'un député démissionnaire": "PARTIELLE-DEM",
    "élection partielle, remplacement d'un député démissionnaire d'office": "PARTIELLE-DEMOFF",
    "élection partielle, remplacement d'un député élu au Parlement européen": "PARTIELLE-PE",
    "élection partielle, remplacement d'un député élu au Sénat": "PARTIELLE-SEN",
    "élection partielle, suite à l'annulation de l'élection d'un député": "PARTIELLE-ANN",
}


def circonscription(d):
    lieu = d.get("election", {}).get("lieu", {})

    if (dep := lieu.get("numDepartement")) and (numero := lieu.get("numCirco")):
        return f"{dep}-{numero}"


spec_extraction_mandat = {
    "id_mandat": "uid",
    "id_personne": S.uid,
    "prenom": S.prenom,
    "nom": S.nom,
    "legislature": "legislature",
    "circonscription": circonscription,
    "suppleante": Coalesce("suppleants.suppleant.suppleantRef", default=""),
    "date_debut": "mandature.datePriseFonction",
    "date_fin": ("dateFin", possiblement_nul),
    "cause_debut_mandat": ("election.causeMandat", CAUSES_MANDATS.get),
    "cause_fin_mandat": "mandature.causeFin",
    "place": "mandature.placeHemicycle",
}

spec_deputees = (
    S(
        uid=Spec(Coalesce("uid.#text", "uid")),
        nom=Spec("etatCivil.ident.nom"),
        prenom=Spec("etatCivil.ident.prenom"),
    ),  # enregistre prenom et nom dans le scope
    "mandats.mandat",  # selectionne les mandats
    to_list,  # convertit en une liste pour les quelques cas de mandats uniques
    Iter()
    .filter(Check("typeOrgane", equal_to="ASSEMBLEE", default=SKIP))
    .map(spec_extraction_mandat),
)


def extraire_mandats(archive, out_file):
    writer = csv.DictWriter(out_file, fieldnames=list(spec_extraction_mandat))

    writer.writeheader()

    mandats = sorted(
        glom(
            json_deputees(archive),
            (Iter(spec_deputees), Flatten()),
        ),
        key=itemgetter("date_debut", "id_mandat"),
    )
    writer.writerows(mandats)


def run():
    archive_path, out_path = sys.argv[1:]

    with ZipFile(archive_path) as archive, open(out_path, "w") as out_file:
        extraire_mandats(archive, out_file)


if __name__ == "__main__":
    run()
