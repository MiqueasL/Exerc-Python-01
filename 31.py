n = int(input('Qual a distancia da viagem ?'))

if n <= 200:
  a = n * 0.50
  print( 'O valor da passagem é R${} '.format(a))
else:
  b = n * 0.45
  print('O valor da passagem é {}'.format(b))

