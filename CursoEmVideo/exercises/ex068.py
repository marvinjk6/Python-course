''' Jogo do Par ou Ímpar

Faça um programa que jogue para o em para com o computador. 
O jogo só será interrompido quando um jogador perder, mostrando total de vitórias consecutivas que ele conquistou no final do jogo

'''
print('=='*30)
print('JOGO PAR OU ÍMPAR - escolha um número de 0 a 10')
print('=='*30)


from random import randint

v = 0
while True:
    player = int(input("Digite um número: "))
    parImpar = input("Par ou Ímpar?? [P/I]: ").strip().lower()
    com = randint(1, 10)
    soma = player + com
    print(f"Você jogou {player}. O computador jogou {com}.\nA Soma é {soma}", end=" ")
    print("Deu PAR" if soma % 2 == 0 else "Deu ímpar")
    if parImpar == "p":
        if soma % 2 == 0:
            print("Você venceu!!! \nVamos jogar novamente...")
            v += 1
        else:
            print("Você PERDEU!!!")
            break
    elif parImpar == "i":
        if soma % 2 == 0:
            print("Você PERDEU!!!")
            break
        else:
            print("Você venceu!!! \nVamos jogar novamente...")
            v += 1
    print("~~" * 30)
print(f"GAME OVER!! Você venceu {v} vezes")
    

