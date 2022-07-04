"""
construcción del archivo de entrenamiento

"""
import pandas as pd
import pickle

from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """

    datos_precios_diarios = pd.read_csv(
        "data_lake/business/features/precios-diarios.csv", index_col=0
    )

    datos_precios_diarios.index = pd.to_datetime(datos_precios_diarios.index)

    n_lags = 60

    list_lags = [0] + list(range(1, n_lags))

    df_lag = datos_precios_diarios.copy()
    df_lags = pd.concat([df_lag.shift(shift) for shift in list_lags], axis=1)
    df_lags = df_lags.dropna()
    df_lags.columns = list_lags
    X = df_lags.copy().drop(columns=[0])
    y = df_lags.copy().iloc[:, [0]]

    (X_train, X_test, y_train, y_test,) = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=1234567,
    )

    pipeline = Pipeline(
        steps=[
            ("Standard", StandardScaler()),
            (
                "PCA",
                PCA(n_components=10),
            ),
            (
                "RandomForestRegressor",
                RandomForestRegressor(n_jobs=-1, random_state=1),
            ),
        ],
    )
    param_grid = {
        "RandomForestRegressor__n_estimators": [200, 500],
        "RandomForestRegressor__max_features": ["auto", "sqrt", "log2"],
    }

    gridSearchCV = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=5,
        scoring="neg_mean_squared_error",
        refit=True,
        return_train_score=True,
    )
    gridSearchCV.fit(X_train, y_train)
    r2_score(y_test, gridSearchCV.predict(X_test))
    pickle.dump(gridSearchCV, open("src/models/precios-diarios.pkl", "wb"))


if __name__ == "__main__":
    import doctest

    train_daily_model()
    doctest.testmod()
