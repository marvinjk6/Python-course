''' MÉDIA ARITMÉTICA
desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

'''
nome = input("Nome do Aluno: ")
n1 = float(input("Digite a Nota 1: "))
n2 = float(input("Digite a Nota 2: "))
media = (n1 + n2) / 2

print("Nome: {} - Nota 1: {} - Nota 2: {} - Média {}".format(nome, n1, n2, media))
