''' Radar eletrônico
Escreva um programa que leia a velocidade de um carro. 
Se eu trapassar 80 km por hora mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$ 7 por cada quilômetro acima do limite
'''

v = float(input("Digite a velocidade que você passou: "))

multa = (v - 80) * 7

if v > 80:
    print('Você excedeu o limite de velocidade que é 80km/h')
    print('terá que pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!!\nDirija com cuidado.')
