''' Interrompendo repetições while

O comando break interrompe um looping quando determinada condição acontecer, no caso quando digitar 999 
'''

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# f-strings
print(f"A soma vale {s}")


'''
## Bônus f-strings
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: R$ "))
print(f"Olá {nome:=^20} , você tem {idade} anos, seu salário é R${salario:.2f}")


## : indica que vai ocupar determinado espaço
## :=>20 -> indica que vai ocupar 20 espaços, alinhado a direita, o sinal de igual vai ocupar o resto dos espaços
## < alinhado a esquerda
## centralizado
'''
