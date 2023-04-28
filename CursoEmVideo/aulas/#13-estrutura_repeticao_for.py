''' Estrutura de repetição for
Estrutura de controle com variável de repetição

A variavel c vai se repetir incrementando o número de vezes que for estabelecido no intervalo:
'range(1, 10)' - importante que o segundo argumento o python não considera nesse caso o intervalo vai de 1 até 9

Se for range(0, 10) aí sim terá 10 repetições, porque vai começar do zero, o 10 é ignorado da mesma maneira, então o intervalo é de 0 a 9

Contar pra traz o terceiro argmento deve ser -1: range(6, 5, -1)

Contar de 2 em 2 o terceiro argumento deve ser 2: range(0, 7, 2)
'''


for c in range(0, 6, 2):
    print(c)