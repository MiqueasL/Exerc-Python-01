largura = float(input('Largura da Parede:'))
altura = float(input('Altura da Parede:'))

metroQuadrado = (largura * altura)

print('A area total e de {} m²'.format(metroQuadrado))
print('Para pinta esta parede sera necessario {}L de tinta'.format(metroQuadrado / 2))