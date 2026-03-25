import click
import polars as pl

COLS = {
    "numero_panneau": "Numéro de panneau",
    "nuance": "Nuance liste",
    "liste_court": "Libellé abrégé de liste",
    "liste": "Libellé de liste",
    "elus_cm": "Sièges au CM",
    "elus_cc": "Sièges au CC",
}


@click.command()
@click.argument("resultats", type=click.Path(exists=True, dir_okay=False))
@click.argument("sieges", type=click.Path(writable=True, dir_okay=False))
def main(resultats, sieges):
    resultats = pl.read_csv(
        resultats,
        separator=";",
        schema_overrides={
            "Code commune": pl.String,
            "Code département": pl.String,
            **{f"Numéro de panneau {i}": pl.Int64 for i in range(1, 14)},
            **{f"Sièges au CM {i}": pl.Int64 for i in range(1, 14)},
            **{f"Sièges au CC {i}": pl.Int64 for i in range(1, 14)},
        },
    )

    n_max = int(resultats.columns[-1].split()[-1])

    selections = [
        {key: f"{value} {i}" for key, value in COLS.items()}
        for i in range(1, n_max + 1)
    ]

    (
        pl.concat(
            [resultats.select(code_commune="Code commune", **s) for s in selections]
        )
        .filter(pl.col("numero_panneau").is_not_null() & (pl.col("elus_cm") != 0))
        .with_columns(pl.col("elus_cc").fill_null(0))
        .sort(["code_commune", "numero_panneau"])
        .write_parquet(sieges)
    )


if __name__ == "__main__":
    main()
