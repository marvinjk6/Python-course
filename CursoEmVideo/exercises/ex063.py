''' Sequência de Fibonacci v1.0


Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

Ex:
0 - 1 - 1 - 2 - 3 - 5 - 8
'''

print('  Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer mostrar? '))

# O primeiro e segundo termos já são definidos (0 e 1)
t1 = 0
t2 = 1 
print("{} → {} → ".format(t1, t2), end="")
cont = 3 # o contador vai começar em três porque os dois primeiros termos  foram mostrados e o 3 será mostrado antes do contador incrementar
while cont <= n:
    t3 = t1 + t2
    print("{}".format(t3), end=" → ")
    t1 = t2 
    t2 = t3
    cont += 1
print("Fim")
print('-'*30)
