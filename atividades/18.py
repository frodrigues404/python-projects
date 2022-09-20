# #obrigatório Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
# se a mesma é uma data válida.



while True:
    data = input("Digite uma data no formato 'dd/mm/aaaa': ")
    if len(data) == 10 and data[2] == '/' and data[5] == '/':
        print("Formato Válido!")
        break
        
        