''' CALCULANDO DESCONTO
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
'''

produto = input("Qual produto você vai adquirir?? ")
preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.05
total = preco - desconto

print('-'*25)
print("Produto: ", produto)
print("Preço: R$ {:.2f}".format(preco))
print("Desconto de 5%: R${:.2f}".format(desconto))
print("Total: R$ {:.2f}".format(total))
print('-'*25)

