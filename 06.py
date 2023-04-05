import math

numero = float(input('Digite um Numero:'))

dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)

print(' O numero {}'.format(numero))
print(' Tem seu dobro {} \n O Triplo {} \n e Sua Raiz é {:.2f}'.format(dobro, triplo, raiz))