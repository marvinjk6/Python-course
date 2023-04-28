''' GAME: Pedra Papel e Tesoura

Crie um programa que faça o computador jogar JoKenPo com você

'''

from random import randint

itens = ("Pedra", "Papel", "Tesoura")
com = randint(0, 2)

print('\033[1;32m {:=^40}'.format(" JokenPo ") )
print('\033[m')
print('''Selecione uma opção:
[0] Pedra
[1] Papel
[2] Tesoura
''')
player = int(input("Qual a sua jogada? "))

print("O computador jogou: {}".format(itens[com]))
print("O jogador jogou: {}".format(itens[player]))

if com == 0:
    if player == 0:
        print("Empatou!!")
    elif player == 1:
        print("O Jogador ganhou!!")
    elif player == 2:
        print("O computador ganhou!!")
    else:
       print('Jogada inválida')
elif com == 1:
    if player == 0:
        print("O computador ganhou!!")
    elif player == 1:
        print("Empatou!!")
    elif player == 2:
        print("O Jogador ganhou!!")
    else:
        print('Jogada inválida')
elif com == 2:
    if player == 0:
        print("O Jogador ganhou!!")
    elif player == 1:
        print("O computador ganhou!!")
    elif player == 2:
        print("Empatou!!")
    else:
       print('Jogada inválida')
else:
       print('Jogada inválida')




    

