num = int(input('Entre com um numero: '))
mult = 0
for i in range(2, num):
    if num % i == 0:
        mult += 1
if mult == 0:
    print('{} é um numero primo!!'.format(num))
elif mult != 0:
    print('{} não é um numero primo!'.format(num))