'''    Aquele clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5: Reprovado 
- Média entre 5 e 6.9: Recuperação 
- Média 7 ou superior: Aprovado
'''


n1 = float(input("Digite a primeira Nota: "))
n2 = float(input("Digite a segunda Nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print("Aluno foi aprovado, sua média foi {:.2f}".format(media))
elif media < 7 and media >= 5:
    print("Aluno de recuperação, sua média foi {:.2f}".format(media))
else:
    print("Aluno foi reprovado, sua média foi {:.2f}".format(media))
    
