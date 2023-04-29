''' Tratando vários valores v1.0

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o Flag)

Flag seria o 999 que é a condição de parada, ele vai ser colocado após a soma e a contagem e assim parar o programa quando ele for digitado

'''

cont = soma = 0
n = int(input("Digite um número [999 se quiser parar]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número [999 se quiser parar]: "))
print("Foram digitados {} números e a soma é {}".format(cont, soma))
