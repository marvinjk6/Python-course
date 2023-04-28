'''Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão

fórmula para saber o qualquer termo de uma PA:
termo = primeiro + (termo-1) * razão
'''

primeiro = int(input("primeiro termo da PA: "))
razao = int(input("Razão: "))
decimo = primeiro + (10-1) * razao


for c in range(primeiro, decimo+ razao, razao):
    print(c, end=" ")
print("\nFIM")