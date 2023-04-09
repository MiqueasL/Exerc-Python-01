velocidade = int(input('Qual a velocidade do seu carro em KM ?'))

multa = (velocidade -80) * 7

if velocidade > 80:
    print('Você ultrapassou os 80km você foi multado, \na multa vai custar R$ {}.'.format(multa))
else:
    print('A veocidade é {}Km Esta tudo OK'.format(velocidade))
