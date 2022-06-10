num = int(input('Entre com o primeior termo da PA: '))
num2 = int(input('Entre com o segundo termo da progressão: '))
r = num2 - num
n = 1
for i in range(0, 10):
    soma = num + (n - 1) * r
    n += 1
    print('Progressão: {}'.format(soma))
print('Razão: ',r)




