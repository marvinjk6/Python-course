'''' Média, Maior e Menor 
Crie um programa que leia vários números inteiros pelo teclado .
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''
n = quant = soma = maior = menor = 0
resposta = "S"
while resposta in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    ## se quantidade de números for igual a 1 ele é o maior e o menor
    if quant == 1: 
        maior = menor = n
    ## caso o cantrario: 
    else:
        ## se o número digitado for maior que o maior, o número que acabou de ser digitado é o maior
        if n > maior:
            maior = n
        ## se o número digitado for menor que o menor, o número que acabou de ser digitado é o menor
        if n < menor:
            menor = n  
    resposta = input("Quer continuar [S/N]??: ").strip()[0]
media = soma / quant
print("Você digitou {} números, a média entre eles é {}".format(quant, media))
print("O menor número digitado foi {} e o maior foi {}".format(menor, maior))
    
