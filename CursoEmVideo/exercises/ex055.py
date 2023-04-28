''' Maior e menor da sequência

Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior peso e o menor peso lidos

'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[1;34mO maior peso é {}kg'.format(maior))
print('\033[1;35mO menor peso é {}kg'.format(menor))
print('\033[m')

