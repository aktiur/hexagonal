from operator import attrgetter
from pathlib import Path

import click

from hexagonal.cog.type_nom import TYPES_NOMS
from hexagonal.files.spec import get_dataframe


@click.command()
@click.argument("chemin_communes", type=click.Path(exists=True, dir_okay=False))
@click.argument("chemin_population", type=click.Path(exists=True, dir_okay=False))
@click.argument("chemin_epci", type=click.Path(exists=True, dir_okay=False))
@click.argument("chemin_communes_epci", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", type=click.Path(dir_okay=False, path_type=Path))
def run(chemin_communes, chemin_population, chemin_epci, chemin_communes_epci, dest):
    communes = get_dataframe(chemin_communes)

    epci = get_dataframe(chemin_epci)
    communes_epci = get_dataframe(chemin_communes_epci)

    communes = communes.merge(communes_epci, how="left")
    communes = communes.merge(epci[["siren_epci", "nom_epci", "type_epci"]])

    if "type_nom" in communes.columns:
        types_noms = communes["type_nom"].map(lambda i: TYPES_NOMS[i])
        communes["forme_possessive"] = (
            types_noms.map(attrgetter("charniere")) + communes["nom"]
        )
        communes["nom"] = (
            types_noms.map(attrgetter("article")).str.capitalize() + communes["nom"]
        )

    population = get_dataframe(chemin_population).iloc[:, :2]
    communes = communes.merge(population, how="left")

    dest.parent.mkdir(parents=True, exist_ok=True)
    communes.to_csv(dest, index=False)


if __name__ == "__main__":
    run()
