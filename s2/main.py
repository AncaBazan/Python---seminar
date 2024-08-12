# liste, tupluri si dictionare
lista = []  # exemplu declarare lista

tuplu = ()  # exemplu declarare tuplu
dictionar = {}  # exemplu declarare dictionar

l = [1, 2, 3, 4.0, 2, "Ana", ['a', 'b', 6], True, False]
for each in l:
    print(type(each), each)

print("lungime lista: ", len(l))
print(l.count(2))
l.remove(2)
print(l)

l.insert(0, "Primul element")
print(l)

# string
s = "python"
for litera in s:
    print(litera)

s1 = s[0:3]
print(s1)

s2 = s[:len(s):2]
print(s2)
s2 = s[1:len(s):2]
print(s2)

s3 = s[::]
print(s3)

# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pare = []
for each in a:
    if each % 2 == 0:
        pare.append(each)
print(pare)

# exemplu de list comprehension
numere_pare = [x ** 2 for x in a if x % 2 == 0]
print(numere_pare)

# dictionare in python
d = {
    "A": 10,
    "B": 8,
    "C": 6
}

print(type(d.keys()), d.keys())
print(type(d.values()), d.values())

lista = [1, 2, 3, 4, 5]
print(list(d.keys())[0])

for k, v in d.items():
    print("{} : {}".format(k, v))
d["A"] = 20
print(d["A"])
# inserare de noi elemente
d["D"] = 30
print(d)
# eliminare de elemente
del d["B"]
print(d)
del d
# print(d) NameError: name 'd' is not defined. Did you mean: 'id'?

lista = list()
lista.append(1)
lista.append(2)
print(lista)

t = (1, 2, 3)
print(type(t), t)

# lambda, filter, map, sort
ridicare_putere = lambda a, b: a ** b

print(ridicare_putere(3, 5))
print(ridicare_putere(2, 2))


