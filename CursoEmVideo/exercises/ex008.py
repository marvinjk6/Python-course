''' CONVERSOR DE MEDIDAS    
Escreva um programa que leia um valor em metros e exiba convertido em cm, mm, dm, dam, hec, Km
'''

metro = float(input("Digite um valor em metros: "))

mm = metro * 1000
cm = metro * 100
dm = metro * 10
dam = metro / 10
hec = metro / 100
km = metro /1000

print("{}mm".format(mm))
print("{}cm".format(cm))
print("{}dm".format(dm))
print("{}dam".format(dam))
print("{}hec".format(hec))
print("{}km".format(km))
