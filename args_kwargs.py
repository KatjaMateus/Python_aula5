def cadastro(*args):
    for arg in args:
        print(arg)

cadastro("Katja", "Kirsi", "Marita")
print(cadastro)

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} : {valor}")

minha_funcao(nome="Katja", idade=53, cidade="Fortaleza")

def minha_funcao(*args,**kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

minha_funcao("Fortaleza", "professora", nome="Katja", idade=53)
