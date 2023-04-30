''' Maior e menor valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla
'''

from random import randint 

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os números sorteados são: ")
for c in numeros:
    print(c, end=" ")

print(f"\nO maior número sorteado é {max(numeros)}")
print(f"O menor número sorteado é {min(numeros)}")

