"""
Ce fichier comprend la routine permettant de nettoyer les fichiers électoraux des scrutins post 2017

Le format employé après 2017 est un CSV à nombre de champs variable (sauf pour les scrutins nationaux où les
candidatures sont partout les mêmes).

Il y a une ligne par bureau de vote avec un certain nombre de champs fixes donnant les informations propres au
bureau de vote (identifiants INSEE, nombre d'inscrits, nombre de bulletins exprimés, etc.) et ensuite les champs
correspondant aux informations d'un candidat sont répétées autant de fois que nécessaire.

Le format est toujours à peu près le même, mais les entêtes utilisés semblent changer quasiment à chaque scrutin… Les
deux tables de correspondance normalisent les noms de champs.
"""

import csv
import sys

import pandas as pd

# la variété des noms d'entête utilisés donne le tournis
fixed_headers = {
    "Code localisation": None,
    "Libellé localisation": None,
    "Code du département": "departement",
    "Code département": "departement",
    "Libellé du département": None,
    "Libellé département": None,
    "Libellé de la section électorale": None,
    "Code de la circonscription": "circonscription",
    "Code circonscription législative": "circonscription",
    "Libellé de la circonscription": None,
    "Libellé circonscription législative": None,
    "Code du canton": "canton",
    "Libellé du canton": None,
    "Libellé du canton": None,
    "Code de la commune": "commune",
    "Code commune": "code_commune",
    "Libellé de la commune": None,
    "Libellé commune": None,
    "Code du b.vote": "bureau",
    "Code B.Vote": "bureau",
    "Code BV": "bureau",
    "Inscrits": "inscrits",
    "Abstentions": None,
    "% Abs/Ins": None,
    "% Abstentions": None,
    "Votants": "votants",
    "% Vot/Ins": None,
    "% Votants": None,
    "Blancs": "blancs",
    "% Blancs/Ins": None,
    "% Blancs/inscrits": None,
    "% Blancs/Vot": None,
    "% Blancs/votants": None,
    "Nuls": None,
    "% Nuls/Ins": None,
    "% Nuls/inscrits": None,
    "% Nuls/Vot": None,
    "% Nuls/votants": None,
    "Exprimés": "exprimes",
    "% Exp/Ins": None,
    "% Exp/Vot": None,
    "% Exprimés/inscrits": None,
    "% Exprimés/votants": None,
    "Etat saisie": None,
}
"""
Comment renommer les entêtes ?
"""

repeated_headers = {
    "N°Panneau": "numero_panneau",
    "N.Pan.": "numero_panneau",
    "N°Liste": "numero_panneau",
    "Numéro de panneau": "numero_panneau",
    "Binôme": "binome",
    "Sexe": "sexe",
    "Sexe candidat": "sexe",
    "Nom": "nom",
    "Nom candidat": "nom",
    "Prénom": "prenom",
    "Prénom candidat": "prenom",
    "Nuance": "nuance",
    "Code Nuance": "nuance",
    "Nuance Liste": "nuance",
    "Nuance liste": "nuance",
    "Nuance candidat": "nuance",
    "Libellé Abrégé Liste": "liste_court",
    "Libellé abrégé de liste": "liste_court",
    "Libellé Etendu Liste": "liste_long",
    "Libellé de liste": "liste_long",
    "Liste": "liste_long",
    "Nom Tête de Liste": "tete_liste",
    "Voix": "voix",
    "% Voix/inscrits": None,
    "% Voix/exprimés": None,
    "% Voix/Ins": None,
    "% Voix/Exp": None,
    "Sièges / Elu": None,
    "Sièges Secteur": None,
    "Sièges CC": None,
    "Sièges": None,
    "Elu": None,
}


transforms = {
    "inscrits": int,
    "votants": int,
    "exprimes": int,
    "blancs": int,
    "voix": int,
    "sexe": "category",
    "numero_panneau": int,
    "numero_liste": int,
    "nuance": "category",
    "nom": "category",
    "prenom": "category",
    "liste_court": "category",
    "liste_long": "category",
    "tete_liste": "category",
}

identifiants = ["code_bureau", "circonscription"]
population = ["inscrits", "votants", "exprimes"]
par_candidat = [
    "numero_panneau",
    "nuance",
    "nom",
    "prenom",
    "sexe",
    "liste_court",
    "liste_long",
    "voix",
]


def read_file(src, delimiter=";", encoding="utf-8"):
    with open(src, "r", encoding=encoding, newline="") as in_file:
        r = csv.reader(in_file, delimiter=delimiter)

        headers = next(r)
        headers = [h.rstrip(" 0123456789") for h in headers]

        common_fields = [h for h in headers if h in fixed_headers]

        # attention aux répétitions
        candidate_specific_fields = []
        for h in headers:
            if h in repeated_headers and h not in candidate_specific_fields:
                candidate_specific_fields.append(h)

        unknown_fields = set(headers).difference(
            common_fields + candidate_specific_fields
        )
        if unknown_fields:
            raise ValueError(f"Champs inconnus : {', '.join(unknown_fields)}")

        fields = [
            fixed_headers[field]
            for field in common_fields
            if fixed_headers.get(field) is not None
        ] + [
            repeated_headers[field]
            for field in candidate_specific_fields
            if repeated_headers.get(field) is not None
        ]

        common_indices = [
            i for i, f in enumerate(common_fields) if fixed_headers[f] is not None
        ]
        candidate_specific_indices = [
            i
            for i, f in enumerate(candidate_specific_fields)
            if repeated_headers[f] is not None
        ]

        all_entries = []

        for line in r:
            common_values = [line[i] for i in common_indices]
            for candidate_offset in range(
                len(common_fields), len(line), len(candidate_specific_fields)
            ):
                candidate_specific_values = [
                    line[candidate_offset + j] for j in candidate_specific_indices
                ]
                if candidate_specific_values[-1] == "":
                    break
                all_entries.append(common_values + candidate_specific_values)

    df = pd.DataFrame(all_entries, columns=fields)

    for field, transform in transforms.items():
        try:
            if field in df.columns:
                df[field] = df[field].astype(transform)
        except ValueError as e:
            print(f"global_fields: {common_fields!r}")
            print(f"repeated_fields: {candidate_specific_fields!r}")
            raise ValueError(f"Echec transformation {transform} sur {field}")

    return df


def clean_results(src, dest, delimiter=";", encoding="utf-8"):
    df = read_file(src, delimiter, encoding=encoding)

    if "code_commune" in df.columns:
        df["code_bureau"] = (
            df["code_commune"].str.zfill(5) + "-" + df["bureau"].str.zfill(4)
        )
    elif "commune" in df.columns:
        df["code_bureau"] = (
            df["departement"].str.zfill(2)
            + df["commune"].str.zfill(3)
            + "-"
            + df["bureau"].str.zfill(4)
        )

    df[
        [c for c in (identifiants + population + par_candidat) if c in df.columns]
    ].to_csv(dest, index=False)


def run():
    src, dest, encoding = sys.argv[1:]
    clean_results(src, dest, encoding=encoding)
