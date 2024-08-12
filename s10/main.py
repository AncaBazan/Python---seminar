import pandas as pd
import numpy as np
from util import *
from acp import AnalizaComponentePrincipale as acp


def execute():
    tabel = pd.read_csv("C:\\Users\\Anca\\Documents\\dsad\\s10\\Freelancer.csv", index_col=0)
    nan_replace(tabel)

    nume_variabile = list(tabel.columns)[2:]

    # construire model ACP + "rulare"
    model = acp(tabel, nume_variabile)
    model.creare_model()

    # interpretare rezultate
    tabel_varianta = model.tabelare_varianta()
    tabel_varianta.to_csv("C:\\Users\\Anca\\Documents\\dsad\\s10\\Varianta.csv")

    model.plot_varianta()

    r_x_c = model.r_x_c
    tabel_rxc = tabelare_matrice(r_x_c, nume_variabile, model.etichete_componente,
                                 "C:\\Users\\Anca\\Documents\\dsad\\s10\\Corelatii_factoriale.csv")

    corelograma(tabel_rxc)

    plot_corelatii(tabel_rxc, "Comp1", "Comp2")
    plot_corelatii(tabel_rxc, "Comp1", "Comp3")

    tabel_componente = tabelare_matrice(model.c, tabel.index, model.etichete_componente,
                                        "C:\\Users\\Anca\\Documents\\dsad\\s10\\Componente.csv")
    plot_componente(tabel_componente, "Comp1", "Comp2")

    # Calcul cosinusuri
    componente_patrat = model.c * model.c
    cosin = np.transpose(componente_patrat.T / np.sum(componente_patrat, axis=1))
    _ = tabelare_matrice(cosin, tabel.index, model.etichete_componente,
                         "C:\\Users\\Anca\\Documents\\dsad\\s10\\Cosin.csv")

    # Calcul comunalitati
    comunalitati = np.cumsum(r_x_c * r_x_c, axis=1)
    tabel_comunalitati = tabelare_matrice(comunalitati, nume_variabile, model.etichete_componente,
                                          "C:\\Users\\Anca\\Documents\\dsad\\s10\\Comunalitati.csv")

    corelograma(tabel_comunalitati, valMin=0, titlu="Comunalitati")
    show()


if __name__ == "__main__":
    execute()
