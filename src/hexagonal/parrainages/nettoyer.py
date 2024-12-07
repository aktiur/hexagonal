import csv
import re
import sys

from glom import glom, Iter

MANDATS = {
    "député": "Députée?",
    "sénateur": "Sénat(eur|rice)",
    "député européen": "Représentante? française? au Parlement européen",
    "conseiller regional": "Conseill(er|ère) régionale?",
    "conseiller departemental": "Conseill(er|ère) départementale?",
    "president epci": "Présidente? d'un EPCI à fiscalité propre",
    "maire": "Maire",
    "maire delegue": "Maire déléguée? d'une commune associée ou d'une commune déléguée",
    "membre assemblee outremer": "Membre d'une assemblée d'une collectivité territoriale d'outre-mer à statut particulier",
    "membre assemblee corse": "Membre de l'Assemblée de Corse",
    "président polynésie française": "Présidente? de la Polynésie française",
    "président nouvelle-calédonie": "Présidente? du gouvernement de la Nouvelle-Calédonie",
    "président martinique": "Présidente? du Conseil exécutif de Martinique",
    "conseiller_paris": "Conseill(er|ère) de Paris",
    "conseiller metropole lyon": "Conseill(er|ère) métropolitaine? de Lyon",
    "maire arrondissement plm": "Maire d'arrondissement",
    "conseiller afe": "Conseill(er|ère) à l'Assemblée des Français de l'étranger",
    "président conseil consulaire": "Présidente? du conseil consulaire",
}

MANDATS = {k: re.compile(f"^{v}$") for k, v in MANDATS.items()}


def normaliser_mandat(mandat):
    return next(k for k, v in MANDATS.items() if v.match(mandat))


spec_parrainages = {
    "mandat": ("Mandat", normaliser_mandat),
    "nom": "Nom",
    "prenom": "Prénom",
    "sexe": ("Civilité", {"M.": "M", "Mme": "F"}.get),
    "circonscription_mandat": "Circonscription",
    "departement_mandat": "Département",
    "candidat": "Candidat",
    "date_publication": "Date de publication",
}


def extraire(in_path, out_path):
    with (
        open(in_path, "r", newline="") as in_fd,
        open(out_path, "w", newline="") as out_fd,
    ):
        r = csv.DictReader(in_fd, delimiter=";")
        w = csv.DictWriter(out_fd, fieldnames=list(spec_parrainages.keys()))

        w.writeheader()
        w.writerows(glom(r, Iter(spec_parrainages)))


def run():
    in_path, out_path = sys.argv[1:]
    extraire(in_path, out_path)


if __name__ == "__main__":
    run()
