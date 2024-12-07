import csv
import re
import sys

from glom import Iter, glom

from hexagonal.codes import outremers
from hexagonal.cog.type_nom import nom_complet_commune

INITIAL_DIGITS = re.compile(r"^\d+")

TYPE_CIRCONSCRIPTIONS = {
    "député": "code_circonscription",
    "sénateur": "code_departement",
    "député européen": "",
    "conseiller régional": "code_departement",
    "conseiller départemental": "code_departement",
    "président epci": "nom_epci",
    "maire": "code_commune",
    "maire délégué": "code_commune",
    "membre assemblée outremer": "code_departement",
    "membre assemblée corse": "code_departement",
    "président polynésie française": "code_departement",
    "président nouvelle-calédonie": "code_departement",
    "président martinique": "code_departement",
    "conseiller paris": "code_departement",
    "conseiller metropole lyon": "code_csp",
    "maire arrondissement plm": "code_commune",
    "conseiller afe": "liste_pays",
    "président conseil consulaire": "nom_consulat",
}


def mapping_commune(cog_departements_path, cog_communes_path):
    with open(cog_departements_path, "r") as fd:
        r = csv.DictReader(fd)

        departements = {d["nom"]: d["code_departement"] for d in r}

    departements.update({outremer.nom: outremer.code_insee for outremer in outremers})
    departements["Français de l'étranger"] = "ZZ"
    departements["Saint-Martin / Saint-Barthélémy"] = "ZX"
    departements["Wallis et Futuna"] = "986"

    with open(cog_communes_path, "r") as fd:
        r = csv.DictReader(fd)

        communes = {}

        for commune in r:
            libelle = nom_complet_commune(commune["nom"], int(commune["type_nom"]))
            communes[commune["code_departement"], libelle] = commune["code_commune"]

    def mapper(parrainage):
        mandat = parrainage["mandat"]
        type_circonscription = TYPE_CIRCONSCRIPTIONS[mandat]

        if not type_circonscription:
            return ""

        if type_circonscription in ["nom_epci", "liste_pays", "nom_consulat"]:
            return parrainage["circonscription_mandat"]

        if type_circonscription == "code_csp":
            return "69M"

        code_departement = departements[parrainage["departement_mandat"]]

        if type_circonscription == "code_departement":
            return code_departement

        if type_circonscription == "code_circonscription":
            numero = (
                INITIAL_DIGITS.match(parrainage["circonscription_mandat"])
                .group(0)
                .zfill(2)
            )
            return f"{code_departement}-{numero}"

        if mandat == "maire arrondissement plm":
            return {"75": "75056", "69": "69123", "13": "13055"}[code_departement]

        code_commune = communes.get(
            (
                code_departement,
                parrainage["circonscription_mandat"],
            )
        )
        if not code_commune:
            return ""

        if type_circonscription == "code_commune":
            return code_commune

        raise ValueError(f"Cas inconnu: ({mandat}, {type_circonscription})")

    return mapper


def qualifier_parrainages(
    clean_parrainages_path, cog_departements_path, cog_communes_path, dest_path
):
    mapper = mapping_commune(cog_departements_path, cog_communes_path)

    spec = {
        "mandat": "mandat",
        "nom": "nom",
        "prenom": "prenom",
        "sexe": "sexe",
        "type_code_circonscription": ("mandat", TYPE_CIRCONSCRIPTIONS.get),
        "code_circonscription": mapper,
        "candidat": "candidat",
        "date_publication": "date_publication",
    }

    with open(clean_parrainages_path, "r") as in_fd, open(dest_path, "w") as out_fd:
        r = csv.DictReader(in_fd)
        w = csv.DictWriter(out_fd, fieldnames=list(spec))
        w.writerows(glom(r, Iter(spec)))


def run():
    clean_parrainages_path, cog_departements_path, cog_communes_path, dest_path = (
        sys.argv[1:]
    )

    qualifier_parrainages(
        clean_parrainages_path, cog_departements_path, cog_communes_path, dest_path
    )


if __name__ == "__main__":
    run()
