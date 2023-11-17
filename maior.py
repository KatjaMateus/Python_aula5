def maior_dos_dois(x,y):
    if x > y:
        return f"O {x} é maior do que o {y}"
    elif y > x:
        return f"O {y} é maior do que o {x}"
    else:
        return f"Os números são iguais"
    
print(maior_dos_dois(5,8))