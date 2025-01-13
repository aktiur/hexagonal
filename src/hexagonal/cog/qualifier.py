from operator import attrgetter
from pathlib import Path

import click

from hexagonal.cog.type_nom import TYPES_NOMS
from hexagonal.files.spec import get_dataset


@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", type=click.Path(dir_okay=False, path_type=Path))
def run(source, dest):
    dataset = get_dataset(source).as_pandas_dataframe()

    if "type_nom" in dataset.columns:
        types_noms = dataset["type_nom"].map(lambda i: TYPES_NOMS[i])
        dataset["forme_possessive"] = (
            types_noms.map(attrgetter("charniere")) + dataset["nom"]
        )
        dataset["nom"] = (
            types_noms.map(attrgetter("article")).str.capitalize() + dataset["nom"]
        )

    dest.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(dest, index=False)


if __name__ == "__main__":
    run()
