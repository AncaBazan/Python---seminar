import pandas as pd
from util import nan_replace


def execute():
    tabel = pd.read_csv("C:\\Anca\\s8\\Freelancer.csv", index_col=0)
    nan_replace(tabel)

    nume_variabile = list(tabel.columns)[2:]

    # creare model ACP + "rulare"

    # interpretare rezultate


if __name__ == "__main__":
    execute()
