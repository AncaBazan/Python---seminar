def filtrare_populatie(x, prag):
    if x[2] < prag:
        return True
    else:
        return False


def filtrare_interval(x, min, max):
    if min < x[3] < max:
        return True
    return False


def sortare_dupa_un_criteriu(x, index):
    return int(x[index])


def sortare_dupa_pib(x):
    return int(x[3])


def inverseaza(a, b):
    aux = a
    a = b
    b = aux


def inverseaza_lista(lista):
    aux = lista[0]
    lista[0] = lista[1]
    lista[1] = aux


vocale = ['a', 'e', 'i', 'o', 'u']
def este_vocala(x):
    if x in vocale:
        return True
    return False