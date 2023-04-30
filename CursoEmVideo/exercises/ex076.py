''' Lista de Preços com Tupla


Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços.
No final mostre uma listagem de preços organizando os dados em forma tabular
'''

listagem = ('Lápis', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 7,
           'Trasnferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 92.39,
           'Canetas', 22.30,
           'Livro', 34.90)


print("-" * 60)
print("{:^60}".format("Listagem de Preços"))
print("-" * 60)


## para resolver esse problema precisamos do índice da tupla, que são números
## com isso é possivel separar em par(nome do produto) e impar(preço)
for pos in range(0, len(listagem)):
    if pos % 2 == 0: # par nome do produto
        # alinhado a esquerda, com pontinhos preenchendo
        print(f"{listagem[pos]:.<47} R$", end="") # não pode quebrar de linha 
    else:
        print(f"{listagem[pos]:>10.2f}")
print("-" * 60)
