''' Soma dos pares

Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas aqueles que forem pares.
Se o valor digitado for impar desconsidere-o
'''
print('\033[1;35m {:=^40}'.format(" Tabuada parte 2 "))
print('\033[m')

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Você digitou {} números pares, a soma deles é {}".format(cont, soma))


print('\033[1;35m {:=^40}'.format(" FIM "))
print('\033[m')