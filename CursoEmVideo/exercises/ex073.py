'''  Tuplas com Times de Futebol

Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol na colocação.
Depois mostre:
- Os cinco primeiros
- Os últimos quatro colocados
- Os times em ordem alfabética
- Em que posição está a Chapecoense
'''

brasileirao = tuple(('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
              'Atlético Paranaense', 'São Paulo', 'Internacional',
              'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
              'Vasco da Gama', 'Atlético-MG', 'Fluminense',
              'Botafogo','Ceará SC', 'Cruzeiro', 'CSA',
              'Chapecoense', 'Avaí'))

print(f"Os cinco primeiros colocados são: {brasileirao[:5]}")
print(f"Os quatro últimos colocados são: {brasileirao[-4:]}")
print(f"A Chapecoense está na posição {brasileirao.index('Chapecoense') + 1}")
print(f"Os times em ordem alfabética: {sorted(brasileirao)}")


