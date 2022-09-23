quantidadeMorangos = float(input("Quantidade de morangos em Kg: "))
quantidadeMacas = float(input("Quantidade de maçãs em Kg: "))
totalKg = quantidadeMacas + quantidadeMorangos

if totalKg <= 5:
    valorMorango = quantidadeMorangos * 2.5
    valorMacas = quantidadeMacas * 1.8
elif totalKg > 5:
    valorMorango = quantidadeMorangos * 2.2
    valorMacas = quantidadeMacas * 1.5
else:
    print("Valor inválido")

print(f'Valor de morangos: R${valorMorango:,.2f}')
print(f'Valor de maçãs: R${valorMacas:,.2f}')