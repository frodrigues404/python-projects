from sys import float_repr_style
from time import sleep

botao = input("ON/OFF: ").upper()

if botao == "ON":
    humidadeInterna = float(input("Humidade interna do forno: "))
    humidadeExterna = float(input("Humidade externa do forno: "))
    temperaturaInterna = int(input("Temperatura interna (ºC): "))
    def aquecerForno(temperatura):
        if temperatura < 200:
            print("Iniciando aquecimento...")
            while(temperatura < 380):
                print(f'{temperatura}ºC...')
                temperatura += 40
                sleep(1)
            print(f'Forno aquecido a {temperatura}ºC')

    def ligarExaustor(humidade):
        if humidade > 15:
            print("Iniciando exaustor...")
            while humidade >= 5:
                print(f'Humidade atual: {humidade}%...')
                sleep(1)
                humidade -= 4
        print(f'A humidade atual é de {humidade}%')


    aquecerForno(temperaturaInterna)
    ligarExaustor(humidadeInterna)



    