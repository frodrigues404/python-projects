from random import *
from random import randint
print("------------")
print("BEM-VINDO(A)")
print("------------")

print('''Opções
[1] Pedra
[2] Papel
[3] Tesoura
[0] SAIR
''')

while True:
    
    jogadaUsuario = int(input("Digite sua jogada: "))
    jogadaCPU = randint(1,3)

    match jogadaUsuario:
        case 1:
            if jogadaCPU == 1:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("EMPATE")
            elif jogadaCPU == 2:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ PERDEU!")
            else:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ VENCEU!")
        
        case 2:    
            if jogadaCPU == 1:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ VENCEU!")
            elif jogadaCPU == 2:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("EMPATE")
            else:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ PERDEU!")
        
        case 3:
            if jogadaCPU == 1:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ PERDEU!")
            elif jogadaCPU == 2:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("VOCÊ VENCEU")
            else:
                print(f'Sua jogada foi {jogadaUsuario} e o programa jogou {jogadaCPU}')
                print("EMPATE!")
        case 0:
            break