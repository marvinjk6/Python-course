''' Número por Extenso


Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
          'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove','Vinte')

n = int(input("Digite um número de 0 a 20: "))
while True:
    n = int(input("Tente novamente. O número precisa estar entre 0 e 20: "))
    if 0 < n <= 20:
        break
print(f"Você digitou o número {numeros[n]}")