concatena = lambda t1, t2 : f"{t1}{t2}" if len(t1) > 5 and len(t2) > 5 else "Erro"

primeira = str(input("Digite a primeira palavra: "))
segunda = str(input("Digite a segunda palavra: "))

print(concatena(primeira, segunda))