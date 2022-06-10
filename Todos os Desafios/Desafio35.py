r1 = int(input('Entre com o tamanho da primeira reta: '))
r2 = int(input('Agora da segunda reta: '))
r3 = int(input('E da terceira reta: '))
if (r1 - r2 < r3) and (r1 + r2 > r3):
    print('É possivel fazer um triangulo com essas retas!')
else:
    print('Não é possivel fazer um triangulo com essas retas!')