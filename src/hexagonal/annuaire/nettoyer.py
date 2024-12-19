import csv
import json
from pathlib import Path

import click
from glom import glom, S, T, Spec, Iter, Coalesce

from hexagonal.utils import nettoyer_avec_spec, iterate_ndjson


def extraire_telephone(telephones):
    return "\n".join(
        f"{t['valeur']} ({t['description']}" if t["description"] else t["valeur"]
        for t in telephones
    )


def selection_adresse(type_adresse):
    return Spec(
        (
            "adresse",
            Coalesce(
                Iter().filter(lambda a: a["type_adresse"] == type_adresse).first(),
                default=None,
            ),
        ),
    )


def extraire_adresse(adresse):
    if adresse:
        elements = [
            adresse["numero_voie"],
            adresse["complement1"],
            adresse["complement2"],
            adresse["service_distribution"],
            f"{adresse['code_postal']} {adresse['nom_commune']}",
        ]

        return "\n".join(e.strip() for e in elements if e.strip())


def coordonnees(adresse):
    if adresse and adresse["longitude"] and adresse["latitude"]:
        return f"{adresse['longitude']},{adresse['latitude']}"


def ouverture(mairie):
    if "plage_ouverture" not in mairie:
        return None

    plages = []

    for p in mairie["plage_ouverture"]:
        deb_jour, fin_jour = p["nom_jour_debut"].lower(), p["nom_jour_fin"].lower()
        deb_hor1, fin_hor1 = p["valeur_heure_debut_1"], p["valeur_heure_fin_1"]
        deb_hor2, fin_hor2 = p["valeur_heure_debut_2"], p["valeur_heure_fin_2"]

        mention_jour = (
            deb_jour if deb_jour == fin_jour else f"du {deb_jour} au {fin_jour}"
        )

        mention_hor = f"{deb_hor1}-{fin_hor1}"
        if deb_hor2:
            mention_hor = f"{mention_hor} et {deb_hor2}-{fin_hor2}"

        plages.append(f"{mention_jour}, {mention_hor}")

    return "\n".join(plages)


spec_mairies = (
    (
        S(
            adresse_physique=selection_adresse("Adresse"),
            adresse_postale=selection_adresse("Adresse postale"),
        )
    ),
    {
        "id": "id",
        "code_commune": "code_insee_commune",
        "siret": "siret",
        "nom": "nom",
        "emails": ("adresse_courriel", "\n".join),
        "adresse_physique": (
            Coalesce(
                S.adresse_physique,
                default=None,
            ),
            extraire_adresse,
        ),
        "adresse_postale": (
            Coalesce(
                S.adresse_postale,
                default="",
            ),
            extraire_adresse,
        ),
        "telephone": ("telephone", extraire_telephone),
        "coordonnees": (Coalesce((S.adresse_physique,), default=None), coordonnees),
        "type_accessibilite": Coalesce(
            S.adresse_physique["accessibilite"],
            default="",
        ),
        "details_accessibilite": Coalesce(
            S.adresse_physique["note_accessibilite"],
            default="",
        ),
        "ouverture": ouverture,
    },
)


spec_conseils_departementaux = (
    (
        S(
            adresse_physique=selection_adresse("Adresse"),
            adresse_postale=selection_adresse("Adresse postale"),
        )
    ),
    {
        "id": "id",
        "code_commune": "code_insee_commune",
        "siret": "siret",
        "nom": "nom",
        "emails": ("adresse_courriel", "\n".join),
        "adresse_physique": (
            Coalesce(
                S.adresse_physique,
                default=None,
            ),
            extraire_adresse,
        ),
        "adresse_postale": (
            Coalesce(
                S.adresse_postale,
                default="",
            ),
            extraire_adresse,
        ),
        "telephone": ("telephone", extraire_telephone),
        "coordonnees": (Coalesce((S.adresse_physique,), default=None), coordonnees),
        "type_accessibilite": Coalesce(
            S.adresse_physique["accessibilite"],
            default="",
        ),
        "details_accessibilite": Coalesce(
            S.adresse_physique["note_accessibilite"],
            default="",
        ),
        "ouverture": ouverture,
    },
)

FICHIERS = [
    ("mairies", spec_mairies),
    ("conseils_departementaux", spec_conseils_departementaux),
]


@click.command()
@click.argument(
    "src_directory",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
)
@click.argument(
    "dest_directory",
    type=click.Path(exists=False, file_okay=False, dir_okay=True, path_type=Path),
)
def run(src_directory, dest_directory):
    dest_directory.mkdir(exist_ok=True, parents=True)

    for fichier, spec in FICHIERS:
        with iterate_ndjson(src_directory / f"{fichier}.json") as it:
            nettoyer_avec_spec(
                it,
                dest_directory / f"{fichier}.csv",
                spec,
                columns=list(spec[1].keys()),
            )


if __name__ == "__main__":
    run()
