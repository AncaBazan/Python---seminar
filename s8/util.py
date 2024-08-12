import pandas as pd


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    nume_variabile = list(t.columns)

    for each in nume_variabile:
        if any(t[each].isna()):
            if pd.api.types.is_numeric_dtype(t[each]):
                t[each].fillna(t[each].mean(), inplace=True)
            else:
                modul = t[each].mode()[0]
                t[each].fillna(modul, inplace=True)