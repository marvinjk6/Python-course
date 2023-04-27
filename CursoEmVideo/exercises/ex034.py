 
''' Aumentos múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250 calcule o aumento de 10%, para os inferiores ou iguais a R$1250 um aumento de 15%
'''

salario = float(input("Digite o salário do funcionário: R$ "))

aumento1 = (salario * 0.10) + salario
aumento2 = (salario * 0.15) + salario

if salario > 1250:
    print("O salário do funcionário com o aumento será de R${:.2f}".format(aumento1))
else:
    print("O salário do funcionário com o aumento será de R${:.2f}".format(aumento2))




