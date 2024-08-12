from clase import Entitate, Tara
from functii import *
# import functii as f


a = 7
b = 5
print(type(a), a, b)
inverseaza(a, b)
print(type(a), a, b)

lista = [a, b]
print(type(lista), lista)
inverseaza_lista(lista)
print(type(lista), lista)

# oop
e1 = Entitate(1, "Romania")
e1.show()
print(e1)

# filter, map, sort
vocale = ['a', 'e', 'i', 'o', 'u']
lista = ['q', 'e', 'r', 't', 'i', 'a', 'o', 'h']
rezultat = []
for litera in lista:
    if litera in vocale:
        rezultat.append(litera)

# filtru
rezultat = filter(lambda x: este_vocala(x), lista)
print(type(rezultat), rezultat)
print(list(rezultat))

# map
sequence = [1, 2, 3, 4, 5]
rezultat = map(lambda x: x**3, sequence)
print(type(rezultat), list(rezultat))

lista_instante = []
lista_tupluri = []

f = open("C:\Anca\s3\dataset.csv", "r")
skip = True
for line in f:
    if skip:
        skip = False
        continue
    cuvinte = line.split(',')
    cuvinte[3] = cuvinte[3].replace('\n', '')
    print(cuvinte)

    lista_tupluri.append(tuple(cuvinte))
    # echivalent Tara(cuvinte[0], cuvinte[1], cuvinte[2], cuvinte[3])
    lista_instante.append(Tara(*cuvinte))


print(lista_tupluri)
for tara in lista_instante:
    print(tara)

lista_instante.sort()
print("\n\n Dupa sortare")
for tara in lista_instante:
    print(tara)

sortata = sorted(lista_tupluri,
                 key=lambda x:sortare_dupa_un_criteriu(x, 2),
                 reverse=True)
print("\n\nsorted")
print(sortata)