from operator import attrgetter
from pathlib import Path

import click

from hexagonal.cog.type_nom import TYPES_NOMS
from hexagonal.files.spec import get_dataset


@click.command()
@click.argument("chemin_communes", type=click.Path(exists=True, dir_okay=False))
@click.argument("chemin_population", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", type=click.Path(dir_okay=False, path_type=Path))
def run(chemin_communes, chemin_population, dest):
    communes = get_dataset(chemin_communes).as_pandas_dataframe()

    if "type_nom" in communes.columns:
        types_noms = communes["type_nom"].map(lambda i: TYPES_NOMS[i])
        communes["forme_possessive"] = (
            types_noms.map(attrgetter("charniere")) + communes["nom"]
        )
        communes["nom"] = (
            types_noms.map(attrgetter("article")).str.capitalize() + communes["nom"]
        )

    population = get_dataset(chemin_population).as_pandas_dataframe().iloc[:, :2]
    communes = communes.merge(population, how="left")

    dest.parent.mkdir(parents=True, exist_ok=True)
    communes.to_csv(dest, index=False)


if __name__ == "__main__":
    run()