numeros = []

numero1 = int(input("Número 1:"))
numeros.append(numero1)
numero2 = int(input("Número 2:"))
numeros.append(numero2)
numero3 = int(input("Número 3:"))
numeros.append(numero3)

numeros.sort()

print(f'{numeros[2]} é o maior número.')
print(f'{numeros[0]} é o menor número.')