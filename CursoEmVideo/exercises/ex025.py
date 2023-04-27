''' Procurando uma string dentro de outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

'''

name = input("Digite seu nome: ").strip().lower()
anwser = "silva" in name

if anwser == True:
    print("Seu nome tem Silva")
else:
    print("Seu nome não tem Silva")
