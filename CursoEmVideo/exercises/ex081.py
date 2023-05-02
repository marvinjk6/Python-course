'''  Extraindo dados de uma Lista

Crie um programa que vai ler varios números e colocar em uma lista. Depois disso mostre:
- Quantos números foram digitados
- A lista de Valores ordenados em forma decrescente
- Se o valor 5 está ou não na lista
'''

lista = []

while True:
    lista.append(int(input("Digite um número: ")))
    
    continuar = input("Quer continuar?? [s/n]: ").strip().lower()[0]
    if "n" in continuar:
        break
print("--" * 20) 
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")
