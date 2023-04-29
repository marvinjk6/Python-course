''' Estrutura de repetição while

Essa estrutura é utilizada quando não sabemos o numero de repetições que será
preciso para executar o programa, mas o while tembém pode ser usado para quando
sabemos número de repetições necessárias

'''

# número de repetições conhecidas
'''
s = 1
while s < 10:
    print(s)
    # precisa acrescentar +1, pois 1 sempre será menor que 10 e irá formar um loop infinito
    s += 1 
'''

# quando não sabemos quantas repetições serão necessárias
s = 0
cont = 0
r = ""
while r in "Ss":
    n = int(input("Digite um número: "))
    r = input("Quer continuar? [S/N]: ")
    s += n
    cont += 1
print("Você digitou {} número(s), a soma desse(s) número(s) é {}".format(cont, s))

