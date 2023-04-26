''' DOBRO - TRIPLO - RAIZ QUADRADA
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada
'''

num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raizQuadrada = pow(num, (1/2))

print("Número: {} \nDobro: {} \nTriplo: {} \nRaiz Quadrada: {}".format(num, dobro, triplo, raizQuadrada))