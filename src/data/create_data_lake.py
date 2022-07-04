"""
Esta función se encarga de crear el data lake con las subcarpetas necesarias
Las carpetas son: landing, raw, cleansed y businnes
"""


def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    """

    import os

    os.mkdir("data_lake")

    directory = [
        "landing",
        "raw",
        "cleansed",
        "business",
    ]

    for carpet in directory:
        os.mkdir(os.path.join("data_lake", carpet))

    dir_business = [
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]

    for carpet in dir_business:
        os.mkdir(os.path.join("data_lake", carpet))

    os.mkdir("data_lake/business/forecasts/")


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()
