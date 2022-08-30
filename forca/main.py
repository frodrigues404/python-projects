from random import *
from random import randint

palavras = ["teste", "ellie", "the last of us"]
palavra = palavras[randint(0, len(palavras) -1)]
palavra_final = "_" * len(palavra)
letrasPalavra = []
letras = []
chances = 5
continuar = True

print(f'Palavra: {palavra}')

while continuar and palavra_final.count("_") > 0:
    palpite = input("Digite uma letra: ")
    letras.append(palpite)
    
    if palpite in palavra and palpite not in letrasPalavra:
        letrasPalavra.append(palpite)
        palavra_final[palavra.find(palpite)].replace("_", palpite)
        print(palavra_final)
        print(letrasPalavra)
        print(f'Palavras ja útilizada: {letras}')
    else:           
        chances = chances - 1
        print(f'{chances} chances restantes.') 
    
    if chances <= 0:
        continuar = False
    