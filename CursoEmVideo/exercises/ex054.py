''' Grupo da Maioridade

Crie um programa que leia o ano de nascimento de 7 pessoas, e no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date

print("\033[1;31m {:=^40}".format(" Grupo da maioridade "))
print("\033[m")

menores = 0
maiores = 0
for c in range(1, 8):
    nasc = int(input("Em que ano nasceu a {}ª pessoa?? Digite: ".format(c)))
    atual = date.today().year
    if atual - nasc >= 18:
        maiores += 1
    else:
        menores += 1
print("Nesse grupo de pessoas {} são maiores e {} são menores.".format(maiores, menores))
