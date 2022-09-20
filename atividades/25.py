# #obrigatório Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
    # a. "Telefonou para a vítima?"
    # b. "Esteve no local do crime?"
    # c. "Mora perto da vítima?"
    # d. "Devia para a vítima?"
    # e. "Já trabalhou com a vítima?"
from turtle import pen


respostas = []

a = input("Telefonou para a vítima? Y/N: ").upper()
respostas.append(a)
b = input("Esteve no local do crime? Y/N: ").upper()
respostas.append(b)
c = input("Mora perto da vítima? Y/N: ").upper()
respostas.append(c)
d = input("Devia para a vítima? Y/N: ").upper()
respostas.append(d)
e = input("Já trabalhou com a vítima? Y/N: ").upper()
respostas.append(e)

positivas = 0
negativas = 0

for c in range(0, len(respostas)):
    if 'Y' in respostas[c]:
        positivas += 1
    elif 'N' in respostas[c]:
        negativas += 1

if positivas == 2:
    print("Suspeito!")
elif 3 <= positivas <= 4:
    print("Cúmplice!")
else:
    print("Culpada!")
