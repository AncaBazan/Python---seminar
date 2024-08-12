import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class AnalizaComponentePrincipale():
    def __init__(self, tabel, nume_variabile=None):
        if nume_variabile is None:
            nume_variabile = list(tabel.columns)

        self._x = tabel[nume_variabile].values

    def creare_model(self, standardizare=True, nlib=0):
        # Pas 1: standardizam setul de date = scadem din fiecare elem media pe coloane si impartim rezultatul la abaterea medie patratica
        if standardizare:
            x_ = (self._x - np.mean(self._x, axis=0)) / np.std(self._x, axis=0)
        else:
            x_ = self._x - np.mean(self._x, axis=0)

        # obtinem dimensiunile setului de date
        n, m = np.shape(self._x)
        # echivalent self._x.shape

        # Pas 2: calculam matricea de covarianta
        r_cov = (1 / (n - nlib)) * x_.T @ x_

        # Pas 3: calcularea vectorilor si valorilor proprii
        valp, vectp = np.linalg.eig(r_cov)

        # ordonam vectorii proprii in ordinea semnificatiei valorilor propii, de la mare la mic
        indici = np.flipud(np.argsort(valp))

        print("valp", valp)
        print("valp[indici]", valp[indici])
        print("vectp", vectp)
        print("vectp[indici]", vectp[indici])

        self._alpha = valp[indici]
        self._a = vectp[:, indici]

        self._c = x_ @ self._a
        self.etichete = ["Comp" + str(i) for i in range(m)]

        # Criterii de identificare a numarului de componente semnificative
        # Kaiser
        predicat = np.where(self._alpha > 1)
        print("predicat Kaiser", predicat)
        print("type predicat", type(predicat))
        self.nr_comp_kaiser = len(predicat[0])
        print("Nr componente cf criteriului Kaiser", self.nr_comp_kaiser)

        # Procent acoperire
        pondere = np.cumsum(self.alpha/ sum(self.alpha))
        predicat = np.where(pondere > 0.8)
        print("predicat Procent", predicat)
        print("type predicat", type(predicat))
        self.nr_comp_procent = predicat[0][0] + 1
        print("Nr componente cf criteriului procent de acoperire", self.nr_comp_procent)

        # Cattell
        # predicat = np.where()
        # print("predicat Cattell", predicat)
        # print("type predicat", type(predicat))
        # self.nr_comp_cattell =
        # print("Nr componente cf criteriului Cattell", self.nr_comp_cattell)

    def tabelare_varianta(self):
        procent_varianta = self.alpha * 100 / sum(self.alpha)

        tabel_varianta = pd.DataFrame(data={
            "Varianta": self.alpha,
            "Varianta cumulata": np.cumsum(self.alpha),
            "Procent varianta": procent_varianta,
            "Procent cumulat": np.cumsum(procent_varianta)
        },
        index=self.etichete)

        return tabel_varianta

    def plot_varianta(self):
        fig = plt.figure("Plot varianta", figsize=(15, 15))
        ax = fig.add_subplot(1, 1, 1)

        ax.set_xlabel("Componente", fontdict={"fontsize": 12, "color": "b"})
        ax.set_ylabel("Varianta", fontdict={"fontsize": 12, "color": "b"})

        m = len(self.alpha)
        gradatii = np.arange((1, m+1))

        ax.set_xticks(gradatii)

        ax.plot(gradatii, self.alpha)
        ax.scatter(gradatii, self.alpha, color="r")

        if self.nr_comp_kaiser is not None:
            ax.axhline(1, c="g", label="Kaiser")

        ax.axhline(self.alpha[self.nr_comp_procent] - 1,
                   c="m", label="Procent acoperire")

        ax.axhline(self.alpha[self.nr_comp_cattell] - 1,
                   c="c", label="Cattell")

        plt.show()

    @property
    def x(self):
        return self._x

    @property
    def alpha(self):
        return self._alpha

    @property
    def a(self):
        return self._a

    @property
    def c(self):
        return self._c

