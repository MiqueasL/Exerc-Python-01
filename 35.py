a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < a + c and c < a +2:
    print('Os segmentos podem formar triangulo')
else:
    print('Os segmentos acima não podem forma triangulo')