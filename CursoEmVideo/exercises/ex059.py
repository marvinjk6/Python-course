''' Criando um Menu de Opções

crie um programa que leia dois valores e mostre um menu como o debaixo:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número número: "))

print('''Escoha uma das opções
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')
escolha = 0

while escolha != 5:
    escolha = int(input("Qual a sua escolha??: "))

    if escolha == 1:
        print("Soma: {} + {} = {}".format(n1, n2, (n1+n2)))
    elif escolha == 2:
        print("Multiplicação: {} x {} = {}".format(n1, n2, (n1*n2)))
    elif escolha == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1, n2))
        elif n2 > n1:
            print("{} é maior que {}".format(n2, n1))
        else:
            print("Os números são iguais")
    elif escolha == 4:
        n1 = int(input("Qual será o primeiro número dessa vez?: "))
        n2 = int(input("E o segundo?: "))
    elif escolha == 5:
        print("Fim do Programa...")
    else:
        print("Opção inválida!!! ")
