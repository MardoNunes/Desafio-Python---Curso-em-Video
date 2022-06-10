num = int(input('Entre com a distancia da sua viajem em Km: '))
if num <= 200:
    preco = num * 0.50
    print('O preço da passagem: {}'.format(preco))
else:
    preco = num * 0.45
    print('O prelo da passagem: {:.0f}'.format(preco))