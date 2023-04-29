''' validação de dados
Faça um programa que leia o sexo de uma pessoa mas só aceite os valores "M" ou "F". Caso esteja errado peça a  digitação novamente até ter um valor correto

'''

sexo = input("Informe o seu sexo [M/F]: ").upper().strip()[0]
while sexo not in "MF":
    sexo = input("Dados inválidos. Digite seu sexo novamente [M/F]: ").upper().strip()[0]
if sexo == "M":
    print("Sexo Masculino registrado")
else:
    print("Sexo Feminino registrado")

