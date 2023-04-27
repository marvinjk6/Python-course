''' ANALISADOR DE TEXTOS
Cri um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas 
- Quantas letras ao todo sem considerar espaços 
- Quantas letras tem o primeiro nome

'''
# strip() para eliminar espaços indesejados nas laterais

name = input("Digite o seu nome completo: ").strip()

print("Seu nome em maiúsculas é: {}".format(name.upper()))
print("Seu nome em minúsculas é: {}".format(name.lower()))
print("Seu nome completo tem {} letras".format(len(name) - name.count(" ")))

# Dividimos o nome com o split(), que vai criar uma lista, pegamos o primeiro valor da lista [0] que corresponde ao primeiro nome, e pegamos o tamanho desse primeiro nome com len()  
primeiroNome = name.split()
print("Seu primeiro nome é {} e tem {} letras".format(primeiroNome[0], len(primeiroNome[0])))



