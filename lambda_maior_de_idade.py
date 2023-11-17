# FAÇA UMA FUNÇÃO LAMBDA QUE RETORNA SE UM USUÁRIO É MAIOR OU MENOR DE IDADE

# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SEU ANO DE NASCIMENTO E USE A FUNÇÃO LAMBDA QUE VOCÊ CRIOU PARA MOSTRAR SE ELE É MAIOR OU MENOR DE IDADE

import datetime
maioridade = lambda ano_nascimento : "Maior de idade" if ano_nascimento >= 18 else "Menor de idade"

ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = datetime.datetime.now().year   #nome de bibioteca = datetime, nome de função dentro dele = datetime

print(maioridade(ano_nascimento))
