''' Analisador completo

Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
No final do programa mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho 
- Quantas mulheres têm menos de 20 anos

'''

somaIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ""
mulherMenosDeVinte = 0

for c in range(1, 5):
    print('------ {}ª Pessoa ------'.format(c)) 
    nome = input("Nome: ").strip()
    idade = int(input("Idade : "))
    sexo = input("Sexo[M/F]: ").strip()
    
    somaIdade += idade

    if c == 1 and sexo in 'Mm':
       maiorIdadeHomem = idade
       nomeHomemMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
       maiorIdadeHomem = idade
       nomeHomemMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        mulherMenosDeVinte += 1
media = somaIdade / 4
print(maiorIdadeHomem)
print(nomeHomemMaisVelho)

print("A media de idade do grupo é {} anos.".format(media))
print("O homem mais velho do grupo é {}".format(nomeHomemMaisVelho))
print("Tem {} mulheres menores de 20 anos".format(mulherMenosDeVinte))




