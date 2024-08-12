import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


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


def tabelare_matrice(x, nume_linii=None, nume_coloane=None, out=None):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    if out is not None:
        t.to_csv(out)
    return t


def corelograma(x, valMin=-1, valMax=1, titlu="Corelatii factoriale"):
    fig = plt.figure(titlu, figsize=(15, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax_ = sb.heatmap(x, vmin=valMin, vmax=valMax,
                     cmap='bwr', annot=True, ax=ax)
    ax_.set_xticklabels(x.columns, rotation=30, ha="right")

    plt.show()


def plot_corelatii(x, var_x, var_y, titlu="Plot corelatii",
                   aspect="auto"):
    fig = plt.figure(titlu, figsize=(15, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)

    theta = np.arange(0, 2 * np.pi, 0.01)
    ax.plot(np.cos(theta), np.sin(theta), color="b")

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(x[var_x], x[var_y], color="r")

    for i in range(len(x)):
        ax.text(x[var_x].iloc[i], x[var_y].iloc[i], x.index[i])

    plt.show()


def plot_componente(x, var_x, var_y, titlu="Plot componente",
                   aspect="auto"):
    fig = plt.figure(titlu, figsize=(15, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)

    ax.scatter(x[var_x], x[var_y], color="r")

    for i in range(len(x)):
        ax.text(x[var_x].iloc[i], x[var_y].iloc[i], x.index[i])

    plt.show()






