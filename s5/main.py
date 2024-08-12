import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


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
    desenare_corelograma(r)

    # desenare corelograma

    # standardizare, normalizare, centrare


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


if __name__ == "__main__":
    execute()