import numpy as np
import pandas as pd
from util import *
import factor_analyzer as fact
from geopandas import GeoDataFrame


def execute():
    tabel = pd.read_csv("C:\\Anca\\s11\\Freelancer.csv", index_col=1)
    nan_replace(tabel)

    nume_variabile = list(tabel)[2:]
    x = tabel[nume_variabile].values

    n, m = x.shape

    # test Bartlett
    test_bartlett = fact.calculate_bartlett_sphericity(x)
    print("Test Bartlett:", test_bartlett)

    if test_bartlett[1] > 0.001:
        print("Nu exista factori comuni")
        exit(0)

    # calul index Kaiser-Meyer-Olkin (KMO)
    kmo = fact.calculate_kmo(x)
    print("KMO", kmo)
    tabel_kmo = pd.DataFrame(data={"Index KMO": np.append(kmo[0], kmo[1])},
                             index=nume_variabile + ["Total"])
    corelograma(tabel_kmo, valMin=0, valMax=1, titlu="Index KMO")

    if all(tabel_kmo["Index KMO"] < 0.6):
        print("Nu exista factori comuni semnificativi")
        exit(0)

    # construire model
    rotatie = ""
    if rotatie == "":
        model_fact = fact.FactorAnalyzer(n_factors=m, rotation=None)
    else:
        model_fact = fact.FactorAnalyzer(n_factors=m, rotation=rotatie)

    model_fact.fit(x)

    # interpretare rezultate
    alpha = model_fact.get_factor_variance()[0]
    etichete_factori = ["F" + str(i+1) for i in range(m)]

    tabel_varianta = tabelare_varianta(alpha, etichete_factori)
    tabel_varianta.to_csv("Varianta_F.csv")

    # corelatii variabile-factori
    loadings = model_fact.loadings_
    tabel_loadings = tabelare_matrice(loadings, nume_variabile, etichete_factori, "Loadings.csv")
    corelograma(tabel_loadings)

    # scoruri factoriale
    sf = model_fact.transform(x)
    tabel_sf = tabelare_matrice(sf, tabel.index, etichete_factori, "SF.csv")
    plot_componente(tabel_sf, "F1", "F2", "Plot scoruri factoriale")

    # calcul comunalitati
    comm = model_fact.get_communalities()
    tabel_comm = pd.DataFrame(data={"Comunalitati": comm}, index=nume_variabile)
    corelograma(tabel_comm, titlu="Comunalitati")

    # harta
    shape = GeoDataFrame.from_file("C:\\Anca\\s11\\World_Simplificat\\World.shp")
    harta(shape, sf[:, :3], "iso_a3", tabel.index)


if __name__ == "__main__":
    execute()