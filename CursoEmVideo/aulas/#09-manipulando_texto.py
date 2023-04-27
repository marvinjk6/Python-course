''' MANIPULANDO TEXTO

Frases para o Python recebe o nome de cadeia de textos ou cadeia caracteres ou string, que sempre estão entre aspas.

Python cria mini-espaços dentro da memória do computador e dentro desses mini-espaço ele vai colocar a letra que vai receber um índice começando pelo zero.

'''


'''------    FATIAMENTO
Significa pegar pedaços de um String 

'''

'''
frase = "Curso em Video Python"

# Nesse caso o espaço 13 não entra na seleção, o Python ignora o ultimo
print("Do 9 até o 12:", frase[9:13])

# Nesse caso ele vai do 9 até o 20, selecionando de 2 em 2 espaços
print("De 2 em 2:", frase[9:21:2])

# Nesse caso ele vai contar do microespaço/índice 0 e até 4, eliminando o 5
print("Do 0 até o 4:", frase[:5])

# Seguindo o mesmo raciocínio do exemplo anterior, vai começar a contar do mini-espaço 15 e vai até o final
print("Do 15 até o final:", frase[15:])

# Vai começar do mini-espaço 9, vai até o final, selecionando de 3 em 3
print("Do 9 até o final de 3 em 3:", frase[9::3])

'''


'''-------  ANÁLISE

Essa é a principal operação que você vai usar, provavelmente. Ela passa informações sobre uma String como por exemplo:
- Qual o tamanho
- Com que letra começa
- Com qual letra termina

''' 

'''
frase = "Curso em Video Python"

# Length significa comprimento, essa função vai mostrar o comprimento da Variável
print(len(frase))

# Nesse caso vai contar quantas letras ‘o’ tem na frase (lembrando que se escrever minúscula, o python vai trazer as minúsculas apenas)
print(frase.count("o"))

# Nesse caso o python vai misturar análise com fatiamento. 
# Vai contar quantas letras ‘o’ tem, do espaço 0, até o 12, pois a última não conta no fatiamento
print(frase.count("o", 0, 13))

# Nessa função ele vai procurar onde começa ‘deo’. Nesse caso no microespaço/índice 11.
print(frase.find("deo"))

# O python vai procurar a string ‘Android’ dentro da variável frase, como não tem o resultado vai ser -1.
# Sempre que o resultado for -1 é porque não existe a string procurada dentro da variável.
print(frase.find("Android"))

#Ele vai mostrar se existe a palavra ‘Curso’ na variável frase. Nesse caso vai mostrar True.
print("Curso" in frase)

'''


'''-------  TRANSFOMAÇÃO

Vai modificar a String

------- ''' 

'''
frase = "Curso em Video Python"

# Ele vai trocar a palavra ‘Python’, por ‘Android’, mas não modifica a frase original
print("Replace: ", frase.replace("Python", "Android"))

# Vai colocar todas as letras para maiúsculas
print("Upper: ", frase.upper())

# Vai colocar todas as letras em minúsculas
print("Lower: ", frase.lower())

# Vai deixar apenas a primeira letra em maiúscula e as demais em minúsculas 
print("Capitalize: ", frase.capitalize())

# Vai colocar a primeira letra de todas as palavras em maiúsculas
print("Title: ", frase.title())

frase2 = "   Aprenda Python   "
print(frase2)

#  Vai tirar os espaços vazios inúteis
print("Strip: ", frase2.strip())

# Vai remover apenas os espaços do lado direito.
print("Strip right: ", frase2.rstrip())

# Vai remover apenas os espaços da esquerda.
print("Strip left: ", frase2.lstrip())
'''

''' --------- DIVISÃO e JUNÇÃO
Funcionalidades de divisão, serve para dividir strings

O Split vai dividir a string da variável em pedaços, e esses pedaços vão receber uma numeração. Além disso cada pedaço vai receber uma sequência nova, tecnicamente o Split cria uma Lista.


'''

frase = "Curso em Video Python"
split = frase.split()
print("Split:", split)


print("Join: ", "-".join(split))






