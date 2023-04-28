''' Contagem regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos artifícios indo de 10 até 0, com uma pausa de 1 segundo entre eles

'''

print('\033[1;31m {:=^40}'.format(" Forgos de Artifício "))
print('\033[m')

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

print("\033[1;35m")
for c in range(0, 6):
    print("Bow!!")
    sleep(0.3)
print('\033[m')