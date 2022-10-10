#BY Guilherme Barea(1127375) e Fernando Rodrigues(1121913)
import random
contador = 0
numerosJogados = []

for n in range(1,7):
    user = int(input(f'Digite o {n}º numero: '))
    numerosJogados.append(user)

numerosJogados.sort()
while True:
    numerosLoteria = []
    while len(numerosLoteria) != 6:
        numsorteado = random.randrange(1, 60)
        if numsorteado not in numerosLoteria:
            numerosLoteria.append(numsorteado)
    
    numerosLoteria.sort()
    contador += 1

    print(f'{contador} jogadas.')
    print(f'Números jogados: {numerosJogados}')
    print(f'Números sorteados: {numerosLoteria}')

    if numerosJogados == numerosLoteria:
        break
    
        