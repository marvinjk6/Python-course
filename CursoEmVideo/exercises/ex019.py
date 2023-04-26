''' Sorteando um da lista

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lembra o nome deles e escrevendo o nome do escolhido.
'''
from random import choice

print("---- Digite o nome dos alunos ----")
a1 = input("Nome do primeiro aluno: ")
a2 = input("Nome do segundo aluno: ")
a3 = input("Nome do terceiro aluno: ")
a4 = input("Nome do quarto aluno: ")

list = [a1, a2, a3, a4]

print("Os alunos são: ")
for aluno in list:
    print(aluno)

print("O aluno sorteado foi - " + choice(list))
