''' Maior e menor valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor

'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando quem é o maior
maior = a
if b > a and b > c:
   maior = b
if c > a and c > b:
   maior = c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))