import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kstest, chisquare


def execute():
    print("Beginning of main")

    # obtinem un set de date
    tabel = pd.read_csv("C:\\Anca\\s5\\Mortalitate.csv", index_col=0)
    # print(type(tabel))
    # print(tabel)

    observatii = list(tabel.index)
    # print(type(observatii))
    # print(observatii)

    variabile = list(tabel.columns)
    # print(type(variabile))
    # print(variabile)

    x = tabel.values
    # print(type(x))
    # print(x)

    # n, m = x.shape
    # print(n, m)

    # prelucrari pe setul de date - completare valori lipsa
    predicat = np.isnan(x)
    # print(predicat)

    coordonate = np.where(predicat)
    # print(coordonate)

    print(x[3, :])
    x[coordonate] = np.nanmean(x[:, coordonate[1]], axis=0)
    print(x[3, :])

    # determinare covarianta si coef de corelatie
    v = np.cov(x, rowvar=False)
    print(v)
    salvare_matrice(v, variabile, variabile, "cov.csv")

    r = np.corrcoef(x, rowvar=False)
    print(r)
    salvare_matrice(r, variabile, variabile, "r.csv")

    # desenare corelograma
    # desenare_corelograma(r)

    # standardizare, normalizare, centrare
    x_std = standardiazare_centrare(x)
    x_c = standardiazare_centrare(x, False)

    salvare_matrice(x_std, nume_randuri=observatii,
                    nume_coloane=variabile, nume_fisier="x_std.csv")
    salvare_matrice(x_c, nume_randuri=observatii,
                    nume_coloane=variabile, nume_fisier="x_c.csv")

    # teste de concordanta
    tabel = teste_concordanta(x)
    nume_coloane = ["s_shapiro", "p_shapiro", "s_ks", "p_ks",
                    "s_chi2", "p_chi2"]
    salvare_matrice(tabel, variabile, nume_coloane, "teste.csv")

    vector_variabile = np.array(variabile)
    decizie_shapiro = tabel[:, 1] > 0.05
    print(decizie_shapiro)
    print("Variabile care urmeaza o distributie normala "
          "conform test Shapiro: ", vector_variabile[decizie_shapiro])

    decizie_ks = tabel[:, 3] > 0.05
    print("Variabile care urmeaza o distributie normala "
          "conform test Kolmogorov Smirnov: ", vector_variabile[decizie_ks])

    decizie_chi2 = tabel[:, 5] > 0.05
    print("Variabile care urmeaza o distributie normala "
          "conform test ChiSquare: ", vector_variabile[decizie_chi2])

def salvare_matrice(x, nume_randuri=None, nume_coloane=None, nume_fisier="out.csv"):
    f = open(nume_fisier, "w")

    if nume_coloane is not None:
        if nume_randuri is not None:
            f.write(',')
        f.write(','.join(nume_coloane) + '\n')

    n = x.shape[0]
    for i in range(n):
        if nume_randuri is not None:
            f.write(nume_randuri[i] + ',')

        f.write(','.join(str(celula) for celula in x[i, :]) + '\n')

    f.close()


def desenare_corelograma(corr, decimals=2,
                         titlu="Corelograma", valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 15))
    plt.title(titlu, fontsize=18, color='r', verticalalignment='bottom')

    sb.heatmap(data=np.round(corr, decimals=decimals),
               vmin = valMin, vmax=valMax, cmap='bwr', annot=True)

    plt.show()


def standardiazare_centrare(x, standardizare=True):
    medii_coloane = np.mean(x, axis=0)
    x_ = x - medii_coloane  # centrare in jurul mediei
    if standardizare:
        abateri_medii_coloane = np.std(x, axis=0)
        x_ = x_ / abateri_medii_coloane  # echivalent: x_ /= abateri_medii_coloane

    return x_


def teste_concordanta(x):
    assert isinstance(x, np.ndarray)

    _, m = x.shape

    tabel = np.empty((m, 6))
    for i in range(m):
        v = x[:, i]
        tabel[i, 0:2] = shapiro(v)  # test Shapiro
        tabel[i, 2:4] = kstest(v, 'norm')  # test Kolmogorov Smirnov
        tabel[i, 4:6] = chisquare(v)  # Chi Square

    return tabel




if __name__ == "__main__":
    execute()