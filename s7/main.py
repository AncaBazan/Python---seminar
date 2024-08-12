import numpy as np
import pandas as pd


def execute():
    tabel_etnii = pd.read_csv("C:\\Anca\\s7\\Ethnicity.csv", index_col=0)
    # apel nan-replace
    nan_replace(tabel_etnii)

    variabile_etnii = list(tabel_etnii.columns)
    print(variabile_etnii)
    variabile_etnii = variabile_etnii[1:]

    # calcul populatie pe etnii la nivel de judet
    tabel_judete = pd.read_excel("C:\\Anca\\s7\\CoduriRomania.xlsx", index_col=0)

    merge1 = tabel_etnii.merge(right=tabel_judete, left_index=True, right_index=True)
    print(merge1)
    merge1.to_csv("C:\\Anca\\s7\\Merge1.csv")

    coloane = variabile_etnii + ["County"]
    print(type(coloane), coloane)
    group1 = merge1[coloane].groupby(by="County").agg(sum)
    group1.to_csv("C:\\Anca\\s7\\EtniiJudete.csv")

    # val = pd.Series(group1[:,18]).max()

    # calcul populatie pe etnii la nivel de regiune
    tabel_regiuni = pd.read_excel("C:\\Anca\\s7\\CoduriRomania.xlsx",
                                 sheet_name="Judete",
                                 index_col=0)

    merge2 = group1.merge(right=tabel_regiuni, left_index=True, right_index=True)
    merge2.to_csv("C:\\Anca\\s7\\Merge2.csv")

    coloane = variabile_etnii + ["Regiune"]
    print(type(coloane), coloane)
    group2 = merge2[coloane].groupby(by="Regiune").agg(sum)
    group2.to_csv("C:\\Anca\\s7\\EtniiRegiuni.csv")

    # calcul populatie pe etnii la nivel de macroregiune
    tabel_macroregiuni = pd.read_excel("C:\\Anca\\s7\\CoduriRomania.xlsx",
                                 sheet_name="Regiuni",
                                 index_col=0)

    merge3 = group2.merge(right=tabel_macroregiuni, left_index=True, right_index=True)
    merge3.to_csv("C:\\Anca\\s7\\Merge3.csv")

    coloane = variabile_etnii + ["MacroRegiune"]
    print(type(coloane), coloane)
    group3 = merge3[coloane].groupby(by="MacroRegiune").agg(sum)
    group3.to_csv("C:\\Anca\\s7\\EtniiMacroRegiuni.csv")

    # indici de di versitate la nivel de localitate
    div_loc = tabel_etnii.apply(func=diversitate, axis=1, denumire_coloana="Localitate")
    div_loc.to_csv("C:\\Anca\\s7\\DiversitateLocalitati.csv")


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


def diversitate(t, denumire_coloana=None):
    assert isinstance(t, pd.Series)
    if denumire_coloana is not None:
        x = np.array(t.iloc[1:], dtype=float)
    else:
        x = np.array(t.values)

    suma = np.sum(x)
    proportii = x / suma

    indici_zero = proportii == 0
    proportii[indici_zero] = 1

    shannon = -np.sum(proportii * np.log(proportii))

    d = np.sum(proportii * proportii)
    simpson = 1 - d
    inverse_simpson = 1/d

    if denumire_coloana is not None:
        serie_div = pd.Series(data=[t.iloc[0], shannon, simpson, inverse_simpson],
                              index=[denumire_coloana, "Shannon", "Simpson", "Inverse_Simpson"])
    else:
        serie_div = pd.Series(data=[shannon, simpson, inverse_simpson],
                              index=["Shannon", "Simpson", "Inverse_Simpson"])

    return serie_div

if __name__ == "__main__":
    execute()