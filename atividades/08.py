# #obrigatório Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input("Valor do primeiro produto: R$"))
produto2 = float(input("Valor do segundo produto: R$"))
produto3 = float(input("Valor do terceiro produto: R$"))

menor = produto1
maior = produto1

if produto2 < menor:
    menor = 'produto 2'
elif produto3 < menor:
    menor = 'produto 3'

print(menor)