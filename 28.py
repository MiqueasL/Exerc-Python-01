from random import randint
n = int(input('Digite um numero entre 0 e 5:'))

numero = randint(0, 5)

if n == numero:
    print('Você venceu')
else:
    print('Você perdeu, eu escolhi o numero {} '.format(numero))