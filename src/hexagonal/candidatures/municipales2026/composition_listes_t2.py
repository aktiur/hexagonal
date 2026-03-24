import click
import polars as pl

from hexagonal.trigram_search import TrigramIndex


def normaliser(colonne):
    if isinstance(colonne, str):
        colonne = pl.col(colonne)
    return (
        colonne.str.normalize("NFKD")
        .str.to_lowercase()
        .str.replace_all(r"\p{Nonspacing Mark}", "")  # diacritiques
        .str.replace_all(r"\pP", " ")  # ponctuation
        .str.replace_all(r"[^a-z0-9 ]+", "")
        .str.replace_all(r"\s\s+", " ")
        .str.strip_chars()
    )


def trouver_correspondances(candidatures_t1, candidatures_t2):
    champs_normalises = {"nom_n": normaliser("nom"), "prenom_n": normaliser("prenom")}

    candidatures_t1 = candidatures_t1.with_columns(**champs_normalises).with_row_index()
    candidatures_t2 = candidatures_t2.with_columns(**champs_normalises).with_row_index()

    jointure_exacte = candidatures_t2.join(
        candidatures_t1,
        on=["code_commune", "sexe", "nom_n", "prenom_n"],
        how="left",
        suffix="_t1",
    )

    candidatures_correspondent = (
        pl.col("index_t1").is_not_null()
        & ~pl.struct("code_commune", "numero_panneau", "ordre").is_duplicated()
    )

    jointure_simple = jointure_exacte.filter(candidatures_correspondent)

    communes_anomalies = jointure_exacte.filter(~candidatures_correspondent)[
        "code_commune"
    ].unique()

    cle_comparaison = normaliser(
        pl.col("prenom")
        + " "
        + pl.col("nom")
        + " "
        + pl.col("nuance").fill_null("NA")
        + " "
        + pl.col("numero_panneau").cast(pl.String)
    ).alias("clé")

    candidatures_t1_restantes = candidatures_t1.filter(
        ~pl.col("index").is_in(jointure_simple["index_t1"].implode())
    ).with_columns(cle_comparaison)

    indexes: dict[str, TrigramIndex[int]] = {}

    for commune in communes_anomalies:
        indexes[commune] = TrigramIndex(
            candidatures_t1_restantes.filter(pl.col("code_commune") == commune)
            .select("clé", "index")
            .rows()
        )

    def mapper(c):
        results = indexes[c["code_commune"]].search(c["clé"], n=1)
        if results:
            return {"score": results[0][0], "index_t1": results[0][1]}
        return None

    rapprochements = (
        candidatures_t2.filter(
            ~pl.col("index").is_in(jointure_simple["index"].implode())
        )
        .with_columns(
            match=pl.struct(pl.col("code_commune"), cle_comparaison).map_elements(
                mapper,
                return_dtype=pl.Struct({"score": pl.Float64, "index_t1": pl.Int64}),
            ),
        )
        .unnest("match")
        .join(
            candidatures_t1_restantes,
            left_on=["index_t1"],
            right_on=["index"],
            how="left",
            suffix="_t1",
        )
    )

    return pl.concat(
        [
            jointure_simple.filter(pl.col("numero_panneau_t1").is_not_null()).select(
                "code_commune",
                "numero_panneau",
                "ordre",
                "numero_panneau_t1",
                "ordre_t1",
            ),
            rapprochements.select(
                "code_commune",
                "numero_panneau",
                "ordre",
                "numero_panneau_t1",
                "ordre_t1",
            ),
        ]
    ).sort(["code_commune", "numero_panneau", "ordre"])


@click.command()
@click.argument(
    "candidatures_t1", type=click.Path(exists=True, readable=True, dir_okay=False)
)
@click.argument(
    "candidatures_t2", type=click.Path(exists=True, readable=True, dir_okay=False)
)
@click.argument(
    "resultats_t1", type=click.Path(exists=True, readable=True, dir_okay=False)
)
@click.argument("composition", type=click.Path(writable=True, dir_okay=False))
@click.argument(
    "composition_nominative", type=click.Path(writable=True, dir_okay=False)
)
def main(
    candidatures_t1, candidatures_t2, resultats_t1, composition, composition_nominative
):
    candidatures_t1 = pl.read_parquet(candidatures_t1)
    candidatures_t2 = pl.read_parquet(candidatures_t2)
    resultats_t1 = (
        pl.read_parquet(resultats_t1)
        .cast({"code_commune": pl.String})
        .group_by(["code_commune", "numero_panneau"])
        .agg(
            pl.col("voix").sum(),
        )
        .with_columns(part=pl.col("voix") / pl.col("voix").sum().over("code_commune"))
    )

    candidatures_t1 = candidatures_t1.join(
        resultats_t1,
        on=["code_commune", "numero_panneau"],
        how="left",
    )

    assert candidatures_t1["part"].is_not_null().all()

    # On ne garde que les listes qui ont fait plus de 5 % au premier tour
    candidatures_t1 = candidatures_t1.filter(pl.col("part") >= 0.05)

    correspondances = trouver_correspondances(candidatures_t1, candidatures_t2)

    correspondances = correspondances.with_columns(
        ordre_t1=pl.when(
            (pl.col("code_commune") == "97617")
            & (pl.col("numero_panneau") == 5)
            & (pl.col("ordre") == 10)
        )
        .then(pl.lit(4))
        .otherwise(pl.col("ordre_t1"))
    )

    correspondances.write_parquet(composition_nominative)

    comp = correspondances.group_by(
        ["code_commune", "numero_panneau", "numero_panneau_t1"]
    ).agg(pl.col("ordre").count().alias("nombre"))

    comp.join(
        candidatures_t2.filter(pl.col("ordre") == 1).select(
            "code_commune", "numero_panneau", "liste", "nuance"
        ),
        on=["code_commune", "numero_panneau"],
    ).join(
        candidatures_t1.filter(pl.col("ordre") == 1).select(
            "code_commune", "numero_panneau", "liste", "nuance"
        ),
        left_on=["code_commune", "numero_panneau_t1"],
        right_on=["code_commune", "numero_panneau"],
        suffix="_t1",
    ).select(
        "code_commune",
        "numero_panneau",
        "liste",
        "nuance",
        "numero_panneau_t1",
        "liste_t1",
        "nuance_t1",
        "nombre",
    ).write_parquet(composition)


if __name__ == "__main__":
    main()
