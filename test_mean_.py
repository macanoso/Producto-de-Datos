import pytest
import pandas as pd

# @pytest.fixture(scope='session')


def import_data():
    df_test = pd.read_csv("data_lake/business/precios-diarios.csv")
    return df_test


def test_data_():
    df_test = import_data()
    expect1 = 118.82415731973808
    assert1 = df_test["precio"].mean()
    print(assert1, expect1)
    assert expect1 == assert1
