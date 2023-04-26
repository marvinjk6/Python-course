''' PINTANDO PAREDE
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
'''

print("Pintando parede")
print("="*15)
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
litros = area / 2

print("A sua parede tem dimensão de {:.2f} x {:.2f}.".format(largura, altura))
print("A área da parede é {:.2f}m².".format(area))
print("Para pintar a parede será necessário {:.1f}L de tinta.".format(litros))

