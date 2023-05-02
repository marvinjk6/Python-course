''' Dividindo valores em várias listas

Crie um programa que vai ler varios números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados respectivamente.
Ao final mostre o conteúdo ase três listas geradas
'''
lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    continuar = input("Quer continuar?? [s/n]: ").strip().lower()[0] 
    if continuar  in "n" :
        break
print("Lista:", lista)

pares = []
impares = []
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print("Números pares da lista: ", pares)
print("Números ímpares da lista", impares)

