''' Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''

cidade = input("Digite o nome da Cidade: ").strip().lower()

if cidade[:5] == "santo": 
    print("o Primeiro nome da Cidade é Santo")
elif cidade[:3] == "são":
    print("o Primeiro nome da Cidade é São")
else: 
    print("A Cidade não começa com o nome Santo ou São")