''' Par ou Ímpar
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
'''

num = int(input("Digite um número qualquer: "))

print("Você digitou o número", num)
if num % 2 == 0:
    print("Esse número é PAR")
else:
    print("Esse número é Ímpar")
