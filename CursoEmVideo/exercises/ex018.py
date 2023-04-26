''' SENO COSSENO E TANGENTE
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

*** No Python as funcionalidades sin = Seno, tan = Tangente e cos = Cosseno aparecem em radianos, por isso é necessário transformar o ângulo que o usuário colocar em radianos


'''

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O Seno vale - {:.2f}".format(seno))
print("O Cosseno vale - {:.2f}".format(cosseno))
print("A Tangente vale - {:.2f}".format(tangente))
