''' Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre o seu fatorial
ex:
3! = 3x2x1 = 6
'''

'''
from math import factorial

n = int(input("Digite um número e veja seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))
'''

'''
# usando for
n = int(input("Digite um número e veja seu fatorial: "))
f = 1
for c in range(n, 0, -1):
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c   
print(f)
'''

# usando While

n = int(input("Digite um número e veja seu fatorial: "))
c = n
f = 1
print("Calculando {}!: ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f)

