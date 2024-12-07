import csv
import sys


def mapping_departement(cog_departements_path):
    with open(cog_departements_path, "r") as fd:
        r = csv.DictReader(fd)

        return {d["nom"]: d["code_departement"] for d in r}


def mapping_commune(cog_communes_path):
    with open(cog_communes_path, "r") as fd:
        r = csv.DictReader(fd)

        return {(d["departement"])}


def run():
    clean_parrainages_path, cog_departements_path, cog_communes_path, dest_path = (
        sys.argv[1:]
    )
