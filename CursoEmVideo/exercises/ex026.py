''' Primeira e última ocorrência de uma string

Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra A 
- Em que posição aparece a primeira vez 
- Em que posição ela aparece pela última vez

'''

frase = input("Digite uma frase: ").strip().lower()

print("A frase tem {} letras 'A'".format(frase.count("a")))
print("A letra 'a' apareceu pela primeira vez na posição {}".format(frase.find("a") + 1))
print('Apareceu pela última vez na posição {}'.format(frase.rfind('a') - frase.count(' ') + 1))


