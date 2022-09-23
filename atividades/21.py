valorSaque = float(input("Valor de saque: R$"))

notas100 = int(valorSaque / 100)
valorSaque = valorSaque % 100

notas50 = int(valorSaque/50)
valorSaque = valorSaque % 50

notas10 = int(valorSaque/10)
valorSaque = valorSaque % 10

notas5 = int(valorSaque/5)
valorSaque = valorSaque % 5

notas1 = int(valorSaque)

print(f'{notas100} notas de 100.')
print(f'{notas50} notas de 50.')
print(f'{notas10} notas de 10.')
print(f'{notas5} notas de 5.')
print(f'{notas1} notas de 1.')