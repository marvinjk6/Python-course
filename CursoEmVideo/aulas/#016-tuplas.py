'''
Tuplas, listas e dicionários são variaveis compostas, ou seja podem receber ou armazenar mais de uma atribuição / valor

As tuplas são imutáveis
podemos iniciar com (), 
ou
essa sintaxe: tuple("valor") vai pegar a string splitar ela
para mais de um valor usamos (()): tuple((valor1, valor2 ...))


'''

lanches = tuple(("Pizza", "Cebola frita", "X-salada", "Batata", "X-bacon", "Carne louca"))

print("Primeiro elemento: ", lanches[0])

# técnica de fatiamento, vai escrever 0, até o 2 mas ignora o 2, portanto a X-salada não aparece
print("Fatiamento:", lanches[0:2])

# segundo elemento até o último
print("Segundo até o último:", lanches[1:])

# Último
print("Último item:", lanches[-1])

# varrendo a tupla
print("Varrendo a tupla: ", end="")
for c in lanches:
    print(c, end=" ")

print("\n")

# Pegando a posição
# 1ª forma
# o enumerate entrega a posição e o valor dessa posição
print("Pegando a posição 1ª forma:")
for pos, c in enumerate(lanches):
    print(f"Lanche: {c} | posição: {pos}")

# 3ª forma
print("Pegando a posição 2ª forma:")
for c in range(0, len(lanches)):
    print(f"Lanche: {lanches[c]} | posição: {c}")

print("\n")

# Para saber a posição que o item está na tupla (index)
print("Posição que está Batata (index):", lanches.index("Batata"))

# Sorted -colocando em ordem alfábetica
print("Em ordem alfabética (sorted): ", sorted(lanches))


# Somando tupla 
a = (2, 5, 4)
b = (5, 8, 1, 2)
c1 = a + b # Simplesmente junta uma na outra
print(c1)

# Mas se Trocar a ordem da soma?
a = (2, 5, 4)
b = (5, 8, 1, 2)
c2 = b + a # A ordem da tupla também troca
print(c2)

# Contar quantas vezes um número tem em uma tupla (count)
print("Quantas vezes o número 5 se repete (count): ", c2.count(5))

## Deletar
# del(c2) só é possível deletar ela inteira

