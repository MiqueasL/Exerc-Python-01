preco = float(input('Qual o valor do produto:'))

calc = ( 5 * preco) / 100

desconto = preco - calc

print('Valor com desconto de {} é {}%'.format(preco, desconto))