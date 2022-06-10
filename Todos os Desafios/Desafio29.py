velocidade = float(input('Entre com a sua volicidade: '))
if velocidade > 80:
    multa = velocidade - 80
    multa = multa * 7
    print('Voce exedeu os limites, multa ${:.1f}'.format(multa))
else:
    print('Parabens, tu anda na lei!!')