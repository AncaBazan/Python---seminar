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

        # Cattell



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

