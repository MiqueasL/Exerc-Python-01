salario = float(input('Qual o valor do salario:'))

if salario >=1250:
    acrescimoA = (10 * salario) / 100
    print('Novo acrescimo do salario {:.2f} e de {:.2f}'.format(salario, acrescimoA + salario))
else:
    acrescimoB = (15 * salario) / 100
    print('Novo acrescimo do salario {:.2f} e de {:.2f}'.format(salario, acrescimoB + salario))