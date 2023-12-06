numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19]
quadrados = list(map(lambda x : x ** 2, numeros))
print(f"A lista de números quadrados é {quadrados}")

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"A lista de números pares é {pares}")

from functools import reduce
soma = reduce(lambda x, y : x + y, numeros)
print(f"A soma dos números é {soma}")