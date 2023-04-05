from math import sin, cos, tan, radians
valor = float(input(' Digite um ângulo:'))

seno = sin(radians(valor))
cosseno = cos(radians(valor))
tangente = tan(radians(valor))


print(' O Ângulo de {} tem \n Seno {:.2f} \n Cosseno {:.2f} \n Tangente {:.2f}'.format(valor, seno, cosseno, tangente))




