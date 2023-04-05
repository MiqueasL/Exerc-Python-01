dias = int(input('Quantidade de dias ?'))
km = float(input('Qual a kilometragem rodada ?'))

apagar = (dias * 60) + (km * 0.15)

print('O valor total a pagar e de {:.2f}'.format(apagar))