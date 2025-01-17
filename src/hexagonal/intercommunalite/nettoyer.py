from pathlib import Path

import click
import pandas as pd

EPCI_COLUMNS = {
    "siren": "siren_epci",
    "dept": "code_departement",
    "raison_sociale": "nom_epci",
    "nature_juridique": "type_epci",
    "mode_financ": "mode_financement",
    "nb_membres": "nombre_membres",
    "total_pop_mun": "population_municipale",
    "total_pop_total": "population_totale",
}

MEMBRES_COLUMNS = {
    "insee": "code_commune",
    "siren_membre": "siren_commune",
    "siren": "siren_epci",
}


@click.command()
@click.argument("src", type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument(
    "epci_dest", type=click.Path(writable=True, dir_okay=False, path_type=Path)
)
@click.argument(
    "communes_epci_dest", type=click.Path(writable=True, dir_okay=False, path_type=Path)
)
def nettoyer(src, epci_dest, communes_epci_dest):
    reference = pd.read_excel(src)

    epci = (
        reference.drop_duplicates("siren")
        .rename(columns=EPCI_COLUMNS)
        .reindex(columns=EPCI_COLUMNS.values())
    )
    epci_dest.parent.mkdir(parents=True, exist_ok=True)
    epci.to_csv(epci_dest, index=False)

    communes_epci = reference.rename(
        columns=MEMBRES_COLUMNS,
    ).reindex(columns=MEMBRES_COLUMNS.values())

    communes_epci_dest.parent.mkdir(parents=True, exist_ok=True)
    communes_epci.to_csv(communes_epci_dest, index=False)


if __name__ == "__main__":
    nettoyer()
