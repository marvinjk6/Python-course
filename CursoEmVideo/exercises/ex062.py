'''  Super Progressão Aritmética v3.0

Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos


'''

print('Gerador de PA')
print('---' * 22)
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10 
while mais != 0:
   total += mais  ## no começo total vai ser igual a 10
   while cont <= total:
       print('{} - '.format(termo), end='')
       termo += razao
       cont += 1
   mais = int(input('\nQuantos termos você quer ver a mais?\n>>>> Digite: '))
print('Progressão finalizada!! {} termos foram mostrados.'.format(total))
