'''   Números primos

Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo

'''

'''
n = int(input("Digite um número: "))

cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print("{} é um número primo".format(n))
else:
    print("{} não é um número primo".format(n))
'''


num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
   if num % c == 0:
       print('\033[1;34m', end='')
       cont += 1
   else:
       print('\033[m', end='')
   print('{}'.format(c), end=' ')
print('\n\033[mO número {}, foi divisível {} vezes.'.format(num, cont))
if cont == 2:
   print('Portanto É Primo')
else:
   print('Portanto NÃO É Primo')