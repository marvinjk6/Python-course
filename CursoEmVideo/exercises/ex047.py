'''  Contagem de pares
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

'''

print('\033[1;32m {:=^40}'.format(" Contagem de Pares "))
print('\033[m')

print("Primeira solução")
for c in range(2, 51, 2):
    print(c, end=" ")
print("\n")

print("Segunda solução")
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=", ")
