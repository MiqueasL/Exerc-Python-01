nome = str(input('Digite seu Nome:')).strip()

letrasQuantidade = len(nome)
divisao = nome.split()
primeirasLetras = len(divisao[0])

print('O nome em maisculo: {}'.format(nome.upper()))
print('O nome em minusculo: {}'.format(nome.lower()))
print('Quantidade de letras no nome: {}'.format(letrasQuantidade))
print('Quantidade letras primeiro nome: {}'.format(primeirasLetras))