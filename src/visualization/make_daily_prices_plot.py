"""
construcción de la gráfica

"""


def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import matplotlib.pyplot as plt
    import pandas as pd

    path_file = r"data_lake/business/precios-diarios.csv"

    daily_data = pd.read_csv(path_file)
    daily_data["fecha"] = pd.to_datetime(daily_data["fecha"])
    fig = daily_data.plot(
        "fecha",
        "precio",
        figsize=(30, 8),
    )
    fig.set_xlabel("Fecha", labelpad=5)
    fig.set_ylabel("Precio")
    fig.set_title("Precios promedios diarios de la electricidad")
    fig.legend(["Promedio Diario"])
    mean = daily_data["precio"].mean()
    plt.axhline(mean, color="r", linestyle="--")
    plt.savefig("data_lake/business/reports/figures/daily_prices.png")


if __name__ == "__main__":
    import doctest

    make_daily_prices_plot()

    doctest.testmod()
