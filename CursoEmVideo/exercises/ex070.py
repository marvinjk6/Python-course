''' Estatísticas em produtos

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final o programa deve mostrar:
- Qual é o total gasto na compra;
- Quantos produtos custam mais de R$ 1000,00; 
- Qual é o nome do produto mais barato

'''

print("=="*30)
print("Digite os nomes e preços dos produtos")
print("=="*30)

total = maisDeMil = cont = 0
barato = ""

''' para verificar qual produto é mais barato é preciso de um contador, que vai ser inicializado apés a leitura do nome e preço do produto, essa primeira ocorrência é a maior e menor, assim é possível fazer a lógica para verificar as demais ocorrências.
'''

while True:
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: R$ "))
    total += preco
    if preco >= 1000:
        maisDeMil += 1
    
    ## lógica para saber o menor preço
    cont += 1
    if cont == 1:
        menor = preco
        barato = nome
    else: 
        if menor > preco:
            menor = preco
            barato = nome

    continuar = " "
    while continuar not in "sn":
        continuar = input("Quer continuar?? [S/N]: ").strip().lower()[0]
    if continuar == "n":
        break
    print('--'*16)
print('**'*30)
print('>> Estatística:')
print(f"Preço total da compra R${total:.2f}")
print(f'Quantidade de produtos com valor maior que R$1000,00: {maisDeMil} Unidade(s)')
print(f'Produto com o menor valor: {barato} custa R${menor:.2f}')