''' Valores únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
- Caso o número á exista dentro da lista ele não será adicionado
- No final serão exibidos todos os valores únicos digitados em ordem crescente
'''

print("-=" * 20)
print("{:^40}".format("Lista de números"))
print("-=" * 20)

continuar = " "
lista = []
while continuar != "n":
    n = int(input("Digite um número: "))
    ## para não repetir valores na lista
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!!!")
    else: 
        print("Valor duplicado!!! Não posso adicionar...")
    continuar = input("Quer continuar?? [S/N]: ")

lista.sort()
print("Lista em ordem: ", lista)
print("Fim")