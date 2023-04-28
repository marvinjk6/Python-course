''' Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
Pergunte o valor da casa, do salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então empréstimo será negado
'''

casa = float(input("Digite o valor total da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Digite em quantos anos você quer pagar: "))

prestacaoMensal =  casa / (anos * 12)
porcentagemSalario = salario * 0.3

if prestacaoMensal >= porcentagemSalario:
    print("Empréstimo negado")
else: 
    print("Empréstimo concedido")
print("O valor da prestação mensal é R${:.2f}".format(prestacaoMensal))
