# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-f-string
"""
Precios diarios de la energia
"""


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd

    file = "data_lake/cleansed/precios-horarios.csv"
    mean_price = pd.read_csv(file)
    mean_price = mean_price.groupby(["fecha"]).mean().reset_index()
    mean_price[["fecha", "precio"]].to_csv(
        "data_lake/business/precios-diarios.csv", encoding="utf-8", index=False
    )


if __name__ == "__main__":
    import doctest

    compute_daily_prices()

    doctest.testmod()
