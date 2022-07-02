# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-f-string
"""
Limpieza de los datos
"""


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo
    data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd

    cleansed_df = []

    for year in range(1995, 2022):
        df_read = pd.read_csv(
            "data_lake/raw/{}.csv".format(year),
        )
        cleansed_df.append(df_read)

    frame = pd.concat(cleansed_df, axis=0, ignore_index=True)
    old_columns = frame.columns
    new_columns = ["fecha"] + ["{0:0=2d}".format(int(i)) for i in old_columns[1:]]
    frame.columns = new_columns

    frame["fecha"] = pd.to_datetime(frame["fecha"], format="%Y-%m-%d")
    unpivoted_table = frame.melt(
        id_vars=["fecha"],
        value_vars=new_columns[1:],
        var_name="hora",
        value_name="precio",
    )
    unpivoted_table["precio"] = unpivoted_table["precio"].fillna(
        unpivoted_table.groupby("fecha")["precio"].transform("mean")
    )
    unpivoted_table.to_csv(
        "data_lake/cleansed/precios-horarios.csv", encoding="utf-8", index=False
    )


if __name__ == "__main__":
    import doctest

    clean_data()
    doctest.testmod()
