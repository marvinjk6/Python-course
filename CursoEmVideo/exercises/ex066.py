'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando Flag)
'''

n = soma = quant = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n == 999:
        break
    soma += n
    quant += 1
print(f"{quant} números foram digitados, a soma entre eles é {soma}")