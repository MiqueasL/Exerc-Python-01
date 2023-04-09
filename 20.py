from random import shuffle

a1 = str(input('Primeiro Aluno:'))
a2 = str(input('Segundo Aluno:'))
a3 = str(input('Terceiro Aluno:'))
a4 = str(input('Quarto Aluno:'))

listaAlunos = [a1, a2, a3, a4]

shuffle(listaAlunos)

print(listaAlunos)

