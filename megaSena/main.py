#BY Guilherme Barea(1127375) e Fernando Rodrigues(1121913)
import random
contador = 0
numerosJogados =[]

for n in range(0,6):
    user=int(input(f'Digite o {n+1}º numero: '))
    numerosJogados.append(user)

numerosJogados.sort()
while True:
    numerosLoteria = []
    while len(numerosLoteria) != 6:
        numsorteado = random.randrange(1, 60)
        if numsorteado not in numerosLoteria:
            numerosLoteria.append(numsorteado)
    
    numerosLoteria.sort()

    print(f'Números jogados: {numerosJogados}')
    print(f'Números sorteados: {numerosLoteria}')

    contador += 1
    print(f'{contador} jogadas.')

    if numerosJogados == numerosLoteria:
        break
    
        