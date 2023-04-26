'''
Módulos possem mais funcionalidades que podemos baixar e usar em nosso projeto

import math - esse comando importa todas as funcionalidades
from math import sqrt, ceill - esse comando importa funcionalidades específicas

Por exemplo o módulo math, que apresenta as seguinte funcionalidades (Métodos)
- Ceil: arredonda o número para cima
- Floor: Arredonda para baixo
- Trunc: vai truncar o número, eliminar a vírgula e o número após ela
- Pow: Calcula a Potência
- Sqrt: Calcula a raiz quadrada
- Factorial: Calcular fatorial
Para usar as funcionalidades use a sintaxe
math.ceil(x)
math.trunc(x)


import random
Shuffle: Vai embaralhar uma lista
Choice: Vai escolher um item de uma lista
Randint: vai pegar um número inteiro aleatorio de um determinado intervalo


'''
import math, random

num  = int(input("Digite um número: "))
raiz = math.sqrt(num)
pow = math.pow(num, 2)
fact = math.factorial(num)

print(raiz, pow, fact)
print("--" * 20)

floatNum = float(input("Digite um número flutuante: "))
ceil = math.ceil(floatNum)
floor = math.floor(floatNum)
trunc = math.trunc(floatNum)
print(ceil, floor, trunc)

print("--" * 20)
print(random.randint(1, 10)) #número inteiro aleatorio de 1 até 10
print(random.random())
