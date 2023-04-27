'''  Jogo da Adivinhação v.1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário o venceu ou perdeu
'''
from random import randint

print("-=" * 23)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=' * 23)

num =  int(input("Digite um número: "))

com = randint(0, 5)
print("Número do computador", com)

if num == com:
    print("Parabéns você acertou!!! :)")
else:
    print("Dessa vez você não acertou :( kkkkkk")


