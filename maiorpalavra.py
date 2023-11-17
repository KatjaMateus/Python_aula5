def palavra_longa(lista):

    maior_palavra = ""      #quando retorno é a palavra

    for item_da_vez in lista:
        if len(item_da_vez) > len(maior_palavra):
            maior_palavra = item_da_vez

    return maior_palavra

    # maior_palavra = 0    #quando retorno é quantidade de letras
    # for i in lista:
    #     if len(i) > maior_palavra:
    #         maior_palavra = len(i)

    # return maior_palavra


lista = []
while True:
    palavra=str(input("Digite uma palvra: "))
    if palavra == "sair":
        break
    else:
        lista.append(palavra)

maior = palavra_longa(lista)

print(maior)