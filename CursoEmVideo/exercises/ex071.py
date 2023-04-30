''' Simulador de Caixa Eletrônico
Crie um programa que simula o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas células de cada valor serão entregues

OBS: Considere que o caixa possui cédulas de 50, 20, 10, e 1 reais
'''

print("==" * 30)
print("{:^60}".format("Bem vindo ao Caixa Eletrônico"))
print("==" * 30)
# é preciso de um montante com o total - variavel total
# a cédula precisa começar pelo maior valor no caso 50 - variavel cedula
# o total de cédulas de cada valor - totalCedula

valor = int(input("Qual o valor do saque?? R$ "))
total = valor 
totalCedula = 0
cedula = 50

while True:
    if total >= cedula: # comparando com os valores das cedulas
        total -= cedula # vai retirando até ficar igual ao valor da cedula
        totalCedula += 1 # vai calcular o número de cédulas
    else:
        if totalCedula > 0:
            print(f"Total de {totalCedula} cedulas de R${cedula:.2f}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('='*30)
print('Obrigado por utilizar o caixa eletrônico')
