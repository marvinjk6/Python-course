''' Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: Binário, Octal ou Hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções abaixo para conversão:
[ 1 ] para conversão em BINÁRIO
[ 2 ] para conversão em OCTAL
[ 3 ] para conversão em HEXADECIMAL''')

opcao = int(input('Escolha sua opção: '))

if opcao == 1:
   print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
   print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
   print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
   print('Opção inválida, tente novamente')

''' Funções usadas:

bin(num)[2:]
oct(num)[2:]
hex(num)[2:]

Para eliminar 0b, 0o e 0x que representa cada base numérica coloque[2:], que fará o fatiamento mostrando a partir do segundo mini-espaço, lembrando que a contagem começa do 0 no Python.


'''