usuario = lambda x : "Erro! Usuário deve ser definido" if x == "" else "Nome deve ter mais de 4 dígitos" if len(x) < 4 else "Usuário cadastrado com sucesso!"
nome = str(input("Digite nome de usuário: "))
print(usuario(nome))