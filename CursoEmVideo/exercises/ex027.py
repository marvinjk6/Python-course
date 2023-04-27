''' Primeiro e último nome de uma pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente

'''

nome = input("Digite su nome completo: ").strip().split()

print("Seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[-1]))
#print('Seu último nome é {}'.format(nome[len(nome) - 1]))

