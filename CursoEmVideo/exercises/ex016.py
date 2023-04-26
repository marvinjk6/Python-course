''' Quebrando um número
Crie um programa que leia um número flutuante e que mostra apenas sua parte inteira
'''
from math import trunc 

num = float(input("Digite um número flutuante: "))
t = trunc(num)

print("A parte inteira de {} é {}".format(num, t))
