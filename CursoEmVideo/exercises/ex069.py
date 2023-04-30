''' Análise de dados do grupo

Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final e mostre:
- Quantas pessoas tem mais de 18 anos 
- Quantos homens foram cadastrados 
- Quantas mulheres têm menos de 20 anos

'''

print("==" * 30)
print("Cadastro de pessoas")
print("==" * 30)

homem = mulherMenosDeVinte = mais18 = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = " " ## muito importante colocar um espaço entre as aspas
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if sexo == "M":
        homem += 1 
    if idade >= 18:
        mais18 += 1
    if sexo == "F" and idade < 20:
        mulherMenosDeVinte += 1
    continuar = " " ## muito importante colocar um espaço entre as aspas
    while continuar not in "SN":
        continuar = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    print("~~" * 30)
    if continuar == "N":
        break
print(f"{mais18} pessoas possuem 18 anos ou mais.")
print(f"Foram cadastrados {homem} homens.")
print(f"Das mulheres cadastradas {mulherMenosDeVinte} possuem menos de 20 anos ")
    
