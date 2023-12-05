from functools import reduce
lista = [34, 56, 6, 78, 79]
maior_numero = reduce(lambda x, y : x if x > y else y, lista)

print(maior_numero)