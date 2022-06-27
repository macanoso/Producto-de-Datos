from ast import excepthandler


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd
    import os

    path = "data_lake/landing"
    FichList = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for f in FichList:
        if f.split(".")[1] == "xlsx":
            df_read = pd.read_excel(
                "data_lake/landing/{}".format(f),
                index_col=None,
                header=None,
            )
            df_read = df_read.dropna(axis=0, thresh=10)
            df_read = df_read.iloc[1:]
            df_read = df_read[df_read.columns[0:25]]
            df_read[0] = pd.to_datetime(df_read[0], format="%Y/%m/%d")
            df_read.to_csv(
                "data_lake/raw/{}.csv".format(f.split(".")[0]),
                encoding="utf-8",
                index=False,
                header=True,
            )
        else:
            df_read = pd.read_excel(
                "data_lake/landing/{}".format(f),
                index_col=None,
                header=None,
            )
            df_read = df_read.dropna(axis=0, thresh=10)
            df_read = df_read.iloc[1:]
            df_read = df_read[df_read.columns[0:25]]
            df_read[0] = pd.to_datetime(df_read[0], format="%Y/%m/%d")
            df_read.to_csv(
                "data_lake/raw/{}.csv".format(f.split(".")[0]),
                encoding="utf-8",
                index=False,
                header=True,
            )


if __name__ == "__main__":
    import doctest

    transform_data()
    doctest.testmod()
