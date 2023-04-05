from math import hypot
from math import sqrt
catetoO = float(input('Medida do cateto oposto:'))
catetoA = float(input('Cateto adjacente:'))

hipotenusa = hypot(catetoO, catetoA)
print('A hipotenusa é {:.2f}'.format(hipotenusa))