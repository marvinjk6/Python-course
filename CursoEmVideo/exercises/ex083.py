''' Validando expressões matemáticas

Crie um programa onde o usuário de digite uma expressão qualquer que use parênteses.
Sua aplicação deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

'''

## A expressão será uma
expressao = input("Digite a expressão: ")
pilha = list()

for simb in expressao:
    if simb == "(":
        # se existir ( na expressão, vai adicionar o parenteses na pilha
        pilha.append("(") 
    elif simb == ")":
        if len(pilha) > 0: 
            # se ) existir na expressão, e o tamanho da pilha for maior que 0, vai remover '(' adicionado anteriormente, isso indica que um par de parenteses foi formado
            pilha.pop()
        else: # se a pilha estiver vazia, adiciona '(' que vai deixar a pilha com um elemento
            pilha.append(")")
            break
## checando se a pilha está vazia - indica que o par de parenteses foi removido, portanto a expressão está correta
if len(pilha) == 0:
    print("Sua expressão está válida!!")
else:
    print("Sua expressão está errada!!")

    