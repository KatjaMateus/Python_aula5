def maior_dos_tres(x,y,z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
    else:
        return x     
    
    
num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
num3=int(input("Digite o terceiro número: "))

maior = maior_dos_tres(num1,num2,num3)

print(f"O maior número divido por 2 é {maior/2}")