''' Sorteando uma ordem na lista

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

'''

from random import shuffle 

print("---- Digite o nome dos alunos ----")
a1 = input("Nome do primeiro aluno: ")
a2 = input("Nome do segundo aluno: ")
a3 = input("Nome do terceiro aluno: ")
a4 = input("Nome do quarto aluno: ")

list = list((a1, a2, a3, a4))
shuffle(list)
print("A Ordem de apresentação é:")

i = 1

for aluno in list:
    print("{}º {}".format(i, aluno))
    i+=1

print("--" * 20)