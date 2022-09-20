from operator import le


vogais = ['a', 'e', 'i', 'o', 'u']
letra = input("Digite uma letra: ").lower()
if letra in vogais:
    print(f"A letra '{letra}' é volgal!")
else:
    print(f"A letra '{letra}' não é volgal!")