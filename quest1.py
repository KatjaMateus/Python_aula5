par_impar = lambda num : f"O {num} é par" if num % 2 == 0 else "impar"

num = int(input("Digite um número: "))

print(par_impar(num))