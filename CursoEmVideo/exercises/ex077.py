'''' Contando vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras.
Depois disso você deve mostrar para cada palavra quais são as suas vogais
'''

palavras = ("aprender", "programar", "linguagem", "python", "curso",
            "grátis", "estudar", "praticar", "tecnologia")

## cada palavra dentro da tupla é uma lista de letras, é possível varrer cada palavra

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos", end=" ")
    for letra in p:
        if letra.lower() in "aáãâeéêiíoóôõuúû":
            print(letra, end=" ")