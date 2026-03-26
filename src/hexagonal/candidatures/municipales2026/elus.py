import polars as pl
import click


@click.command()
@click.argument("sieges_t1", type=click.Path(readable=True, dir_okay=False))
@click.argument("sieges_t2", type=click.Path(readable=True, dir_okay=False))
@click.argument("candidats_t1", type=click.Path(readable=True, dir_okay=False))
@click.argument("candidats_t2", type=click.Path(readable=True, dir_okay=False))
@click.argument(
    "composition_nominative", type=click.Path(readable=True, dir_okay=False)
)
@click.argument("elus", type=click.Path(writable=True, dir_okay=False))
def main(
    sieges_t1, sieges_t2, candidats_t1, candidats_t2, composition_nominative, elus
):
    sieges_t1 = pl.read_parquet(
        sieges_t1, columns=["code_commune", "numero_panneau", "elus_cm", "elus_cc"]
    )
    sieges_t2 = pl.read_parquet(
        sieges_t2, columns=["code_commune", "numero_panneau", "elus_cm", "elus_cc"]
    )
    candidats_t1 = pl.read_parquet(candidats_t1).with_columns(
        ordre_cc=pl.when(pl.col("candidat_communautaire")).then(
            pl.col("ordre")
            .rank(method="ordinal")
            .over(["code_commune", "numero_panneau", "candidat_communautaire"])
        )
    )
    candidats_t2 = pl.read_parquet(candidats_t2).with_columns(
        ordre_cc=pl.when(pl.col("candidat_communautaire")).then(
            pl.col("ordre")
            .rank(method="ordinal")
            .over(["code_commune", "numero_panneau", "candidat_communautaire"])
        )
    )
    composition_nominative = pl.read_parquet(composition_nominative)

    listes_t1 = candidats_t1.unique(["code_commune", "numero_panneau"]).select(
        "code_commune",
        pl.col("numero_panneau", "liste", "nuance").name.suffix("_t1"),
    )

    candidats_t1 = (
        candidats_t1.join(
            sieges_t1,
            on=["code_commune", "numero_panneau"],
            validate="m:1",
        )
        .filter(
            (pl.col("ordre") <= pl.col("elus_cm"))
            | (pl.col("ordre_cc") <= pl.col("elus_cc"))
        )
        .with_columns(
            elu_cm=pl.col("ordre") <= pl.col("elus_cm"),
            elu_cc=((pl.col("ordre_cc") <= pl.col("elus_cc")).fill_null(False)),
        )
        .select(
            "code_commune",
            "nom",
            "prenom",
            "sexe",
            "elu_cm",
            "elu_cc",
            pl.col("numero_panneau", "liste", "nuance", "ordre").name.suffix("_t1"),
        )
    )

    candidats_t2 = (
        candidats_t2.join(
            sieges_t2,
            on=["code_commune", "numero_panneau"],
            validate="m:1",
        )
        .filter(
            (pl.col("ordre") <= pl.col("elus_cm"))
            | (pl.col("ordre_cc") <= pl.col("elus_cc"))
        )
        .with_columns(
            elu_cm=pl.col("ordre") <= pl.col("elus_cm"),
            elu_cc=((pl.col("ordre_cc") <= pl.col("elus_cc")).fill_null(False)),
        )
        .join(
            composition_nominative,
            on=["code_commune", "numero_panneau", "ordre"],
            validate="1:1",
        )
        .join(
            listes_t1,
            on=["code_commune", "numero_panneau_t1"],
            validate="m:1",
        )
        .select(
            "code_commune",
            "nom",
            "prenom",
            "sexe",
            "elu_cm",
            "elu_cc",
            "numero_panneau_t1",
            "liste_t1",
            "nuance_t1",
            "ordre_t1",
            pl.col("numero_panneau", "liste", "nuance", "ordre").name.suffix("_t2"),
        )
    )

    candidats = pl.concat([candidats_t2, candidats_t1], how="diagonal").sort(
        ["code_commune", "numero_panneau_t1", "ordre_t1"]
    )

    candidats.write_parquet(elus)


if __name__ == "__main__":
    main()
