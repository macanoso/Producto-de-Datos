"""
construcción de la predicción

"""


def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import os
    import pandas as pd
    import pickle
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score
    from sklearn.ensemble import RandomForestRegressor

    datos_precios_diarios = pd.read_csv(
        "data_lake/business/features/precios_diarios.csv", index_col=0
    )
    datos_precios = datos_precios_diarios.copy()
    datos_precios.index = pd.to_datetime(datos_precios_diarios.index)

    n_lags = 60

    list_lags = [0] + list(range(1, n_lags))

    df_lag = datos_precios.copy()
    df_lags = pd.concat([df_lag.shift(shift) for shift in list_lags], axis=1)
    df_lags = df_lags.fillna(0)
    df_lags.columns = list_lags
    X = df_lags.copy().drop(columns=[0])
    y = df_lags.copy().iloc[:, [0]]

    model_gs = pickle.load(open("src/models/precios-diarios.pkl", "rb"))
    prediction = model_gs.predict(X)

    datos_precios_diarios["Prediction"] = prediction

    datos_precios_diarios.to_csv(
        "data_lake/business/forecasts/precios-diarios.csv",
    )


if __name__ == "__main__":
    import doctest

    make_forecasts()

    doctest.testmod()
