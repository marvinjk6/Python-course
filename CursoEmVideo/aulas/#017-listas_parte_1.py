'''  Listas parte 1

Listas podem ser modificadas
criar listas = []



'''

lanches = ["hamburguer", "suco", "pizza", "pudim"]
# modificando
#lanches[3] = "cookie"
#print("Trocando pudim por cookie: ", lanches)

# inserindo um elemento por último
#lanches.append("Batata frita")
#print("Append: ", lanches)

# inserindo um elemento em uma posição específica
#lanches.insert(2, "açaí")
#print("Insert: ", lanches)

# removendo o último elemento
#lanches.pop()
#print("Pop: ", lanches)

# removendo elemento com um índice específico
#lanches.pop(2)
#print("Removendo o segundo elemento - pop(2): ", lanches)

# Tamanho da lista
#print("Tamanho len: ", len(lanches))

# removendo com remove que recebe valores - se existir valor repetido vai eliminar a primeira ocorrência
#lanches.remove("hamburguer")
#print("Removendo com remove(): ", lanches)

'''
# removendo se o valor existir
if "pudim" in lanches:
    lanches.remove("pudim")
    print(lanches)
else:
    print("açaí não está na lista")
'''

'''
# pegando valor e posição da lista - 1ª maneira
for c in range(0, len(lanches)):
    print(f"Posição: {c} | valor: {lanches[c]}")
print("-=" * 15)

# pegando valor e posição da lista - 2ª maneira
for pos, valor in enumerate(lanches):
    print("Posição: {} | valor: {}".format(pos, valor))
print("-=" * 15)
'''


'''
# Criando uma lista sequencial com um intervalo
#numeros = list(range(0, 5))
#print(numeros)

numeros = list((14, 2, 33, 25, 44, 59))

# colocando a lista em ordem
numeros.sort()
print("Colocando em ordem sort():", numeros)

# colocando em ordem reversa
numeros.sort(reverse=True)
print("Em ordem reversa:", numeros)

# varrendo uma lista
for c in numeros:
    print(c)
print("-=" * 15)
'''


'''
# pedindo dados ao usuário e colocando esses dados na lista

lista = list()
for c in range(1, 5):
    lista.append((input("Digite o item: ")))
for pos, valor in enumerate(lista):
    print(f"Na posição {pos} encontrei o item {valor}")
print("Fim")
'''

# quando uma variavel é associada a outra variável que é uma lista
#as duas variáveis passam a fazer referencia a mesma lista 
a = [2, 3, 4, 7]
b = a
print(a, b)

# se modificar uma, a outra também será modificada
b[0] = 1000
print("Lista a:", a)
print("Lista b:", b) 


## fazendo uma cópia de uma lista
lista = ["mesa", "cadeira", "panela"]
copia = lista[:]

print("lista: ", lista)
print("cópia: ", copia)








