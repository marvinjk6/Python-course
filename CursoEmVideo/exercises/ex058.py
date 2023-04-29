''' Jogo da Adivinhação v2.0

melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer
'''

from random import randint
from time import sleep
print("-=-=-= Vou pensar em um núemro tente adivinhar -=-=-=-=-")


p = 1
com = randint(1, 10)
n = int(input("Qual o seu palpite?? "))

print("Processando...")
sleep(2)
while n != com:
   p += 1
   if n < com:
        n = int(input("O número que o computador pensou é maior.\nTente de novo: ")) 
   else:
        n = int(input("O número que o computador pensou é menor.\nTente de novo: "))
if p == 1:
    print("Você acertou de Primeira!!!")
else:
    print("Agora você acertou!!!\nVocê precisou de {} Tentativas".format(p))