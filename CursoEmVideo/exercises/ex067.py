''' Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompida quando o número solicitado for negativo
'''

n = 0
while True:
    n = int(input("Digite um número e veja sua tabuada: "))

    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c:2} = {n * c}")
    print('-'*40)
print("================== Fim ==================")

