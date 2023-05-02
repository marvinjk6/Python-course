'''  Maior e Menor valores na Lista

Faça um programa que leia 5 valores numéricos iguais guarde-os em uma lista.
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

'''

print("-=" * 20)
print("{:^40}".format("Lista de 5 números"))
print("-=" * 20)

lista = list()

maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f"Digite um número para a posição {c}: ")))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print("Lista: ", lista)
 
print(f"O maior valor da lista é {maior}, na(s) posição(s):", end=" ")
## pegar a posição, precisa varrer a lista
for pos, v in enumerate(lista):
    if v == maior:
        print(f"{pos}...", end=" ")

print(f"\nO menor valor da lista é {menor}, na(s) posição(s): ", end="")
for pos, v in enumerate(lista):
    if v == menor:
        print(f"{pos}...",  end=" ")

print("\nMin:", min(lista))
print("Max:", max(lista))


