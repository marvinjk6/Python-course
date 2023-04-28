''' Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim 
- Até 14 anos: Infantil
- Até 19 anos: Júnior 
- Até 25 anos: Sênior
- Acima: Master

'''

from datetime import date

nasc = int(input("Digite o ano que você nasceu: "))
atual = date.today().year
idade = atual - nasc

print("O atleta nasceu em {}, tem {} anos.".format(nasc, idade))
if idade > 25:
    print("Está na categoria Master")
elif idade <= 25 and idade > 19:
    print("Está na categoria Sênior")
elif idade <=19 and idade > 14:
    print("Está na categoria Junior")
elif idade <= 14 and idade > 9:
    print("Está na categoria Infantil")
else:
    print("Está na categoria Mirim")




