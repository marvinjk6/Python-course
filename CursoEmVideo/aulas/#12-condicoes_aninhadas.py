'''  Condiçoes aninhadas
Se quiser mais uma condição, é só acrescentar mais um elif,é possível acrescentar quantos você quiser. Lembrando que é obrigatório ter um if e começar com o if.
O else é opcional e só pode aparecer uma vez.

'''

nome = input("Digite o seu nome: ").strip().title()

if nome == 'Marvin':
   print('Olá {}, que nome bonito!!'.format(nome))
elif nome in 'João Thainá Gabriel Paulo':
   print('{}, seu nome é bem popular!!'.format(nome))
else:
   print('Que nome comum {}, brincadeira kkk'.format(nome))
print('Prazer em te conhecer!! ')