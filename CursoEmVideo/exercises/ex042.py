''' Analisando Triângulos Parte 2

Refaça o desafio 035 dois triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais 
- Isósceles: dois lados iguais 
- Escaleno: todos os lados diferentes

End='' indica que O print que estiver na linha de baixo, vai aparecer na linha que está o End=''


Variações de como fazer, que serviriam para outras linguagens
Equilátero
a == b and b == c


Escaleno
a != b and a != c and b=! c

Isósceles
a == b != c or a == c != b or b == c != a


'''

print("=*" * 22)

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Os lados podem formar um triângulo, ", end='Tipo: Triângulo ')
    if a == b == c:
        print("Equilátero")
    elif a != b != c != a:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os lados não podem formar um Triângulo.")

print("=*" * 22)

