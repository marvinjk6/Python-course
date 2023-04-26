''' CONVERSOR DE MOEDAS
Crie um programa que leia quanto dinheiro uma pessoa tem e mostra quantos dólares ela poderia comprar
considere US$ 1.00 = R$3.27
'''

real = float(input("Quantos Reais você tem?? R$ "))

dolar = real / 3.27

print("Com R${:.2f} é possível comprar US${:.2f}".format(real, dolar))

