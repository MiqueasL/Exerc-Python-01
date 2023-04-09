letra = str(input('Digite um frase:')).lower().lower()

letraA = letra.split()

print('A letra "A" aparece {} vezes'.format(letra.count('a')) )
print('A letra "A" apareceu a primeira vez na posição {}'.format(letraA[0:].count('a')))
print('A ultima posição da letra "A" e {}'.format(letra[5:].count('a')))
