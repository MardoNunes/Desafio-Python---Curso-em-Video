produto = float(input('Entre com o preço do produto: '))
desconto = (5*produto)/100
novo_produto = produto - desconto
print('Preço do produto com o desconto de 5%: {:.2f}'.format(novo_produto))


