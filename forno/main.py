from sys import float_repr_style
from time import sleep

botao = input("ON/OFF: ").upper()

if botao == "ON":
    humidadeInterna = float(input("Humidade interna do forno: "))
    temperaturaInterna = int(input("Temperatura interna (ºC): "))
    def aquecerForno(temperatura, temperaturaDesejada):
        if temperatura < 200:
            print("Iniciando aquecimento...")
            while(temperatura < temperaturaDesejada):
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


    print("Iniciando processo de desumidificação...")
    sleep(2)
    if temperaturaInterna > 15 and humidadeInterna >= 40:
        ligarExaustor(humidadeInterna)
    elif temperaturaInterna < 15 and humidadeInterna >= 40:
        aquecerForno(temperaturaInterna, 100)
        ligarExaustor(humidadeInterna)
    print("Processo concluído")
    print("Iniciando processo de cocção...")
    sleep(2)
    humidadeInterna = float(input("Humidade interna do forno: "))
    ligarExaustor(humidadeInterna)

    temperaturaInterna = int(input("Temperatura interna (ºC): "))
    if temperaturaInterna < 200:
        aquecerForno(temperaturaInterna, 380)

    iniciar = input("Inserir conteúdo para cocção - quando contluir presisionar o botão pronto: ").upper()
    if iniciar == "PRONTO":
        sleep(10800)

    print(f'A temperatura atual do forno é de {temperaturaInterna}ºC e a humidade interna é de {humidadeInterna}ºC.')



    