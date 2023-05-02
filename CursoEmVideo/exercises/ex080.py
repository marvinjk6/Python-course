'''  Lista ordenada sem repetições

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção, (sem usar sort()) 
No final mostre a lista ordenada na tela
'''

print("-=" * 20)
print("{:^40}".format("Lista de 5 números"))
print("-=" * 20)

lista =[]
for c in range(0, 5):
    n = int(input("Digite um valor: "))

    # vai checar se:
    # o c for igual ao zero 
   
    # vai dar um append(n) que adiciona no final
    if c == 0: 
        lista.append(n)
        print("Primeiro valor adicionado!!")
    # o n é maior que o último valor da lista len(lista -1)
    elif n > lista[-1]:
        lista.append(n)
        print("Valor adicionado no final da Lista")
    else:
        pos = 0
        while pos < len(lista):
            ## se o n (número que quero inserir é menor) que lista[pos]
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Valor adicionado na posição {pos}")
                break ## vai inserir apenas uma vez, e sair do while
            pos += 1
print("Os valores digitados em ordem são: {}".format(lista))


        
