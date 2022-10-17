from func import lerNumero, clear, lerArquivo, registrar
clear()

nome = input("Nome: ").upper()
idade = lerNumero("Idade: ", "Valor inválido", int)

if idade >= 18:

    dados = lerArquivo()
    dados.append(f'{nome}, {idade}\n')
    registrar(dados)

    print(f'{nome}, registro efetuado com sucesso.')
else:
    print("Não pode ser cadastrado")