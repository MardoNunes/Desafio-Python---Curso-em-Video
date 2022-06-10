ano = int(input('Entre com um ano: '))
if (ano % 4 == 0) and (ano % 1000 != 0):
    print('{} é bissexto'.format(ano))
else:
    print('Não é um ano bissexto!')