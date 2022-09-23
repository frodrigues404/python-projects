produto1 = float(input("Valor do primeiro produto: R$"))
produto2 = float(input("Valor do segundo produto: R$"))
produto3 = float(input("Valor do terceiro produto: R$"))

produtos = [produto1, produto2, produto3]

produtos.sort()

print(produtos)

print(f'O menor produto é de R${produtos[0]}')
print(f'O maior produto é de R${produtos[2]}')