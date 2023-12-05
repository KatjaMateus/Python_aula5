nomes = ["João", "Maria", "Carolina", "Sid", "MIckey"]

nomes_grandes = list(filter(lambda x: len(x) > 5, nomes))
print(nomes_grandes)