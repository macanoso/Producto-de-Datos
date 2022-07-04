"""
construcción de la predicción

"""


def carga_pickle():
    """
    Cargue el modelo entrenado final.
    """
    import pickle

    with open("precios-diarios.pkl", "rb") as f:
        model = pickle.load(f)
    return model


def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import pickle as pkl
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score

    datos_precios_diarios = pd.read_csv(
        "data_lake/business/features/precios_diarios.csv", index_col=0
    )

    datos_precios_diarios.index = pd.to_datetime(datos_precios_diarios.index)

    n_lags = 60

    list_lags = [0] + list(range(1, n_lags))

    data_train = datos_precios_diarios.copy()

    df_lag = datos_precios_diarios.copy()
    df_lags = pd.concat([df_lag.shift(shift) for shift in list_lags], axis=1)
    # df_lags = df_lags.dropna()
    df_lags.columns = list_lags
    X = df_lags.copy().drop(columns=[0])
    y = df_lags.copy().iloc[:, [0]]

    model = carga_pickle()
    prediction = model.predict(X)

    r2_score(y, prediction.predict(X))

    datos_precios_diarios["Prediction"] = prediction

    datos_precios_diarios.to_csv(
        "data_lake/business/forecasts/precios-diarios.csv", index=None
    )


if __name__ == "__main__":
    import doctest

    make_forecasts()

    doctest.testmod()
