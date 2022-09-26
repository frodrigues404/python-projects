numeros = []
numero1 = int(input("Número 1: "))
numeros.append(numero1)
numero2 = int(input("Número 2: "))
numeros.append(numero2)
numero3 = int(input("Número 3: "))
numeros.append(numero3)

numeros.sort(reverse=True)

for c in range(0, 3):
    print(numeros[c])