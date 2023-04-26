''' ALUGUEL DE CARROS
Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dia pelos quais ele foi alugado. 
Calcule o preço a pagar sabendo que o carro custa R$60,00 por dia e R$0,15 centavo por quilômetro rodado

'''

dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros foram percorridos? "))

preco = (60 * dias) + (km * 0.15)

print("Após a análise o valor a ser pago é: R${:.2f}".format(preco))