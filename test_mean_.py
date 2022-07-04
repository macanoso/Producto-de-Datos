"""
Esta funciona testea el promedio de los precios de los productos
"""
# pylint: disable=unused-import

import pytest
import pandas as pd

# @pytest.fixture(scope='session')


def import_data():
    """
    Importa los datos de la tabla unica de precios horarios.
    """
    df_test = pd.read_csv("data_lake/business/precios-diarios.csv")
    return df_test


def test_data_():
    """
    Esta funciona testea el promedio de los precios de los productos
    """
    df_test = import_data()
    expect1 = 118.82415731973808
    assert1 = df_test["precio"].mean()
    print(assert1, expect1)
    assert expect1 == assert1
