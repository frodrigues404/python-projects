from random import *
from random import randint

palavras = ["turistas", "protesto", "elegante", "telefone", "barbeiro", "olhos"]
palavra = palavras[randint(0, len(palavras) -1)]
palavra_final = "_" * len(palavra)
letrasPalavra = []
letras = []
chances = 5
continuar = True

print(f'A palavra contem {len(palavra)} letras.')
print(palavra_final)
print(f'Palavra: {palavra}') #Teste temporário

while palavra_final.count("_") > 0:
    palpite = input("Digite uma letra: ")
    letras.append(palpite)
    
    if palpite in palavra and palpite not in letrasPalavra:
        letrasPalavra.append(palpite)
        #print(palavra_final[palavra.find(palpite)])
        #palavra_final = palavra_final.replace(palavra_final[palavra.find(palpite)], palpite)
        palavra_final[palavra.find(palpite)].replace("_", palpite)
        print(palavra_final)
        print(letrasPalavra)
        print(f'Letras ja útilizada: {letras}')
    else:           
        chances = chances - 1
        print(f'{chances} chances restantes.') 

    if chances <= 0:
        break