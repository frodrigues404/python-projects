import os

def lerArquivo():
    try:
        arquivo = open("bd.txt", "r")
    except:
        arquivo = open("bd.txt", "w")
        arquivo.close()
        arquivo = open("bd.txt", "r")

    dados = arquivo.readlines()
    arquivo.close()
    return dados

def registrar(dados):
    arquivo = open("bd.txt", "w")
    arquivo.writelines(dados)


def lerNumero(msgInicial, msgErro, type):

    while True:
        try:
            valor = type(input(msgInicial))
            return valor
        except:
            clear()
            print(msgErro)

def clear():
    os.system("cls")