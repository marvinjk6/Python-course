''' Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/check: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal 
- 3x ou mais no cartão: 20% de juros

^ - centralizado
{:^40} - centralizado em 40 espaços
'''
print('\033[1;36m {:=^40}'.format(' Loja do Marvin '))

##                  fim da cor
preco = float(input("\033[mPreço das compras: R$ "))

print('''Selecione a opção de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual a opção de pagamento: "))

if opcao == 1:
    desconto = (preco * 0.1)
    total = preco - desconto
    print("Você teve um desconto de 10% - R${:.2f}".format(desconto))

elif opcao == 2:
    desconto = (preco * 0.05)
    total = preco - desconto
    print("Você teve um desconto de 5% - R${:.2f}".format(desconto))

elif opcao == 3:
    total = preco
    parcelas = preco / 2
    print("Você irá pagar duas parcelas de {:.2f}".format(parcelas))
elif opcao == 4:
    juros = preco * 0.2
    total = preco + juros
    vezes = int(input("Quantas vezes: "))
    parcelas = total / vezes
    print("Você terá que pagar 20% de juros - R$ {:.2f}".format(juros))
    print("Você irá pagar {} parcelas de R$ {:.2f}".format(vezes, parcelas))
else:
    print("Opção inválida")
print("Valor total da compra R$ {:.2f}".format(total))


