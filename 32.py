ano = int(input('Digite o ano:'))

calculo = ano % 4

if calculo == 0:
    print('O ano {} e bissexto'.format(ano))
else:
    print('O ano {} não e bissexto'.format(ano))