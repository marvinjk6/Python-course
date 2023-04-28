'''  Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade você ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo no alistamento.
Seu programa também deverá mostrar o tempo que falta o que passou do prazo

'''

from datetime import date

nascimento = int(input("Digite o ano que você nasceu: "))
anoAtual = date.today().year
idade = anoAtual - nascimento
anoAlistamento = nascimento + 18

if idade == 18:
    print('''Você nasceu em {}, portanto tem {} anos.
Precisa se alistar esse ano!!'''.format(nascimento, idade))
elif idade > 18:
    print('''Você nasceu em {}, portanto tem {} anos.
Se ainda não se alistou deveria ter feito isso há {} anos!!
Seu alistamento foi no ano de {}. '''.format(nascimento, idade, idade - 18,anoAlistamento))
else:
    print('''Você nasceu em {}, portanto tem {} anos.
Falta(m) {} anos para você se alistar!!
Você terá que se alistar em {}.'''.format(nascimento, idade, 18 - idade, anoAlistamento))



