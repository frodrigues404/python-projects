nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))

media = (nota1+nota2) / 2

if media >= 7 and media <= 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media > 10 :
    print("Aprovado com distinção") 