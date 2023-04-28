''' Tabuada (parte 2)

Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for
 
'''
print('\033[1;34m {:=^40}'.format(" Tabuada parte 2 "))
print('\033[m')

n = int(input("Digite um número e veja sua tabuada: "))

print('=' * 40)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n*c)))


print('\033[1;34m {:=^40}'.format(" FIM "))
print('\033[m')