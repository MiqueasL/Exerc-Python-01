a = str(input('Nome completo:')).strip()

b = a.split()

print('Primeiro nome: {}'.format(b[0]))
print('O ultimo nome {}'.format(b[len(b)-1]))
