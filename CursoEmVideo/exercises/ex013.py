''' REAJUSTE SALARIAL
Faça um programa que leia o salário de um funcionário e mostre o reajuste com 15% de aumento

'''

salario = float(input("Digite o salário do funcionário: R$ "))
salarioReajustado = salario + (salario * 0.15) 

print("O salário do funcionario era R$ {:.2f} \nCom o reajuste o salário fica em R${:.2f}".format(salario, salarioReajustado))