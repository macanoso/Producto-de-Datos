def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import os
    from pathlib import Path

    parent_directory = Path(__file__).parent.parent
    data_lake = os.mkdir(os.path.join(parent_directory, "data_lake"))
    directory = [
        "data_lake/landing",
        "data_lake/raw",
        "data_lake/cleansed",
        "data_lake/business",
    ]

    for d in directory:
        os.mkdir(os.path.join(parent_directory, d))

    dir_business = [
        "data_lake/business/reports",
        "data_lake/business/reports/figures",
        "data_lake/business/features",
        "data_lake/business/forecasts",
    ]

    for d in dir_business:
        os.mkdir(os.path.join(parent_directory, d))


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()
