#Obrigatorio
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if 9 <= media <= 10:
    print(f"\nMédia {media}.\nConteito A.\nAluno aprovado.")
elif 7.5 <= media < 9:
    print(f"\nMédia {media}.\nConteito B.\nAluno aprovado.")
elif 6 <= media < 7.5:
    print(f"\nMédia {media}.\nConteito C.\nAluno aprovado.")
elif 4 <= media < 6:
    print(f"\nMédia {media}.\nConteito D.\nAluno reprovado.")
elif 0 <= media < 4:
    print(f"\nMédia {media}.\nConteito E.\nAluno reprovado.")
else:
    print("Valor inválido")
    