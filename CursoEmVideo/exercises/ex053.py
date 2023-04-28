''' Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.

ex:
Apos a sopa
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona
Ame o poema

Explicando a técnica com for
junto = "".join(palavras) para desconsiderar os espaços, juntando as palavras

range(len(junto) - 1, -1, -1)
explicação len(junto) - 1: deve começar pela ultima letra, se a string tem 10 letras a última está no index 9, então a gente subtrai -1 para começar com a ultima letra
primeiro -1: esse -1 indica que o intervalo vai até 0, que seria a primeira letra, pois o python ignora o segundo argumento do intervalo
segundo -1: o segundo -1 indica que a contagem vai ser de trás para frente de um em um

Explicando a técnica com fatiamento
para inverter a variável junto podemos usar join[::-1]
[::-1] - inicio,  fim, invertido
: (dois pontos) - indica um intervalo  

'''

'''
frase = input("Digite uma frase: ").strip().lower()
palavras = frase.split()
#print(palavras)
junto = "".join(palavras) # vai
#print(junto)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("Junto: " + junto)
print("Inverso: " + inverso)

if inverso == junto:
   print('Temos um palíndromo')
else:
   print('Não é um palíndromo')
'''

## Usando Fatiamento:

frase = input("Digite uma frase: ").strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
if inverso == junto:
   print('Temos um palíndromo')
else:
   print('Não é um palíndromo')
