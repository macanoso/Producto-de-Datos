# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-f-string
"""
Precios diarios de la energia
"""


def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    file = "data_lake/cleansed/precios-horarios.csv"
    mean_price = pd.read_csv(file)
    mean_price["fecha"] = pd.to_datetime(mean_price["fecha"])
    mean_price = (
        mean_price.groupby(pd.Grouper(key="fecha", freq="M")).mean().reset_index()
    )
    mean_price[["fecha", "precio"]].to_csv(
        "data_lake/business/precios-mensuales.csv", encoding="utf-8", index=False
    )


if __name__ == "__main__":
    import doctest

    compute_monthly_prices()

    doctest.testmod()
