''' Analisando Triângulo

desenvolva um programa que leia o cumprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
Lembrando que a soma de dois lados do triângulo deve ser maior que o outro lado restante:

'''

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    print("Essas retas podem formar um triângulo")
else:
    print("Essas retas não podem formar um triângulo")
