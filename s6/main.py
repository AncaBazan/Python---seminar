import numpy as np
import pandas as pd


def execute():
    tabel_etnii = pd.read_csv("C:\\Anca\\s6\\Ethnicity.csv",
                              index_col=0)

    # apel nan-replace

    tabel_localitati = pd.read_excel("C:\\Anca\\s6\\CoduriRomania.xlsx", index_col=0)

    merge1 = tabel_etnii.merge(right=tabel_localitati, left_index=True, right_index=True)






if __name__ == "__main__":
    execute()