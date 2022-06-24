#jogo da adivinhação
# noinspection PyUnresolvedReferences
import random
num = int(input('Entre com um numero de 1 à 10: '))
aux = random.randint(1, 10)
cont = 1
if num != aux:
    while num != aux:
        num = int(input('Entre com um numero de 1 à 10: '))
        aux = random.randint(1, 10)
        cont += 1
    print('Voce precisou de {} tentativas para acertar!'.format(cont))
else:
    print('Boa campeão, voce precisou de 1 tentativa para acertar!')
