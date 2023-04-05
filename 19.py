from random import choice
a1 = str(input('Nome do Aluno:'))
a2 = str(input('Nome do Aluno:'))
a3 = str(input('Nome do Aluno:'))
a4 = str(input('Nome do Aluno:'))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))