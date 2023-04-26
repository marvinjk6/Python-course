''' CONVERSOR DE TEMPERATURA
Escreva um programa que converta a uma temperatura digital em Celsius para Fahrenheit
'''
print("-----"* 13)

c = float(input("Digite o valor da temperatura em °C que será convertido para °F: "))
f = (9 / 5 * c) + 32
print("{:.1f}°C equivale a {:.1f}°F".format(c, f))

fah = float(input("Agora digite o valor de uma temperatura em °F que será convertido para °C: "))
cel = (fah - 32) * 5 / 9
print("{:.1f}°F equivale a {:.1f}°C".format(fah, cel))

print("-----"* 13)

