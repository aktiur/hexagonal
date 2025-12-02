from pathlib import Path
from zipfile import Path as ZPath
from zipfile import ZipFile

import click
import pandas as pd

VALEURS_MANQUANTES = (
    "nd",  # non diffusable
    "ns",
    "so",
    "s",
)

noms_colonnes = {
    "IRIS": "code_iris",
    "DISP_TP6021": "taux_pauvrete_60",
    "DISP_INCERT21": "taux_pauvrete_60_incertitude",
    "DISP_Q121": "quartile1",
    "DISP_MED21": "mediane",
    "DISP_Q321": "quartile3",
    "DISP_EQ21": "ecart_interquartile_mediane",
    "DISP_D121": "decile1",
    "DISP_D221": "decile2",
    "DISP_D321": "decile3",
    "DISP_D421": "decile4",
    "DISP_D621": "decile6",
    "DISP_D721": "decile7",
    "DISP_D821": "decile8",
    "DISP_D921": "decile9",
    "DISP_RD21": "rapport_interdecile_9_1",
    "DISP_S80S2021": "rapport_80_20",
    "DISP_GI21": "indice_gini",
    "DISP_PACT21": "part_revenus_activite",
    "DISP_PTSA21": "part_salaires_traitements",
    "DISP_PCHO21": "part_indemnites_chomage",
    "DISP_PBEN21": "part_revenus_activites_non_salaries",
    "DISP_PPEN21": "part_pensions_retraites_rentes",
    "DISP_PPAT21": "part_revenus_patrimoine",
    "DISP_PPSOC21": "part_prestations_sociales",
    "DISP_PPFAM21": "part_prestations_familiales",
    "DISP_PPMINI21": "part_minima_sociaux",
    "DISP_PPLOGT21": "part_prestations_logements",
    "DISP_PIMPOT21": "part_impots",
    "DISP_NOTE21": "note_precaution",
}


@click.command()
@click.argument(
    "archive_path", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.argument(
    "dest_path", type=click.Path(file_okay=True, dir_okay=False, path_type=Path)
)
def run(archive_path, dest_path):
    dest_path.parent.mkdir(exist_ok=True, parents=True)

    with ZipFile(archive_path) as archive:
        archive_root = ZPath(archive)

        with (archive_root / "BASE_TD_FILO_IRIS_2021_DISP.csv").open(
            "r", newline=""
        ) as fd:
            revenu_disponible = pd.read_csv(
                fd,
                sep=";",
                decimal=",",
                na_values=VALEURS_MANQUANTES,
                dtype={"IRIS": str},
                keep_default_na=False,
            )
            revenu_disponible = revenu_disponible.rename(
                columns=noms_colonnes
            ).convert_dtypes()
            revenu_disponible.to_csv(dest_path, index=False)


if __name__ == "__main__":
    run()
