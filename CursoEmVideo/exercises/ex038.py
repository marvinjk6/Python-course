'''
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro valor é maior 
- O segundo maior é maior 
- Não existe um valor maior os dois são iguais

'''

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print("O primeiro número é maior")
elif n2 > n1:
    print("O segundo número é maior")
else:
    print("Os números são iguais")  