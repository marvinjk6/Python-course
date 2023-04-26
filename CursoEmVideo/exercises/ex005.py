''' ANTECESSOR E SUCESSOR
Faça um programa que leia um número inteiro e mostre no na tela o seu sucessor é seu antecessor

'''
num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print("Número: {}, Antecessor: {}, Sucessor: {}".format(num, ant, suc))