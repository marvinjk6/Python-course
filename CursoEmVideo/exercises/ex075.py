''' Análise de dados em uma Tupla

Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. 
No final mostre:

- Quantas vezes apareceu o valor 9;
- Em que posição foi digitado o primeiro valor 3;
- Quais foram os números pares;
'''

num = (int(input("Digite o primeiro número: " )), int(input("Digite o segundo número: " )), int(input("Digite o terceiro número: " )), int(input("Digite o quarto número: " )))

print(f"O número 9 aparece {num.count(9)} veze(s)")
if 3 in num:
    print(f"O número três está na posição {num.index(3)+1}")
else:
    print("O número três não apareceu nenhuma vez")
print("Os números pares são:")
for c in num:
    if c % 2 == 0:
        print(c, end=" ")

