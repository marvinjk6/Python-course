''' Soma ímpares múltiplos de três

Faça um programa que calcule a Soma entre todos os números ímpares que são múltiplos de 3 e que se encontra no intervalo de 1 até 500
'''

print('\033[1;33m {:=^40}'.format(" Soma ímpares múltiplos de três "))
print('\033[m')

soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        cont += 1
print("A soma dos {} números múltiplos de 3 que estão no intrevalo entre 1 e 500 é: {}".format(cont, soma))

