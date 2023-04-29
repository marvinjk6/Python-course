''' Progressão Aritmética v2.0

Refaça o desafio 051 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura Whille
'''


print('Gerador de PA')
print('---' * 10)

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
s = 0
c = 1
while c <= 10:
    print("{}".format(termo), end=" ")
    termo += razao
    c += 1
print("FIM")

