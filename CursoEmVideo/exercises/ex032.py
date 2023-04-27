''' Ano Bissexto
faça um programa que leia uma ano qualquer me mostre se ele é bissexto

'''

from datetime import date

ano = int(input('Qual ano você quer analisar? Se for o ano atual digite 0: '))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print('O ano {} é BISSEXTO.'.format(ano))
else:
   print('O ano {} NÃO é Bissexto'.format(ano))
