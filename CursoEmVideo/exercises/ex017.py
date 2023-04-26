
''' CALCULANDO HIPOTENUSA
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
'''

from math import hypot
co = float(input("Digite o comprimento do Cateto Oposto: "))
ca = float(input("Digite o comprimento do Cateto Adjacente: "))

hyp = hypot(co, ca)
print('O comprimento da Hipotenusa vale {:.2f}.'.format(hyp))

# Fórmula matemática
# hip = (co ** 2 + ca ** 2) ** 2
