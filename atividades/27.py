quantidadeMorangos = float(input("Quantidade de morangos em Kg: "))
quantidadeMacas = float(input("Quantidade de maçãs em Kg: "))
totalKg = quantidadeMacas + quantidadeMorangos
valorMorango = quantidadeMorangos * 2.5
valorMacas = quantidadeMacas * 1.8
valorTotal = valorMacas + valorMorango

if totalKg > 5:
    valorMorango = quantidadeMorangos * 2.2
    valorMacas = quantidadeMacas * 1.5

if totalKg > 8 and valorMacas + valorMorango > 25:
    print("Aplicando desconto de 10%...")
    valorTotal = valorTotal * 10 / 100

print(f'\nValor a pagar será de: R${valorTotal:,.2f}')
print(f'R${valorMorango} de morangos.')
print(f'R${valorMacas} de maçãs.')
