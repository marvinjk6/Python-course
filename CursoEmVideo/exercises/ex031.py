'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem Comprando R$0,50 por quilômetro para viage de até 200 km e R$0,45 o para viagens mais longas

'''

km = float(input('Digite a distância da viagem para saber o preço da passagem: '))
p1 = km * 0.50
p2 = km * 0.45

if km > 200:
    print("O preço da passagem será R${:.2f}".format(p2))
else:
    print("O preço da passagem será R${:.2f}".format(p1))
