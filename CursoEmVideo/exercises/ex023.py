'''  Separando dígitos de um número

Faça um programa que leia números do 0 a 9999 e mostre na tela cada um dos dígitos separados

'''

n = int(input("Digite um número: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

''' 
A lógica é pegar o número fazer a divisão inteira: ex: 5472 // 10 = 547
E depois vai dividir por 10 e pegar o resto da divisão: 547 % 10 = 54,7 o resto é 7.

'''


