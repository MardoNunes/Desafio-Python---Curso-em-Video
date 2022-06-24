#Fatorial de um numero

num = int(input('Entre com um numero inteiro: '))
aux = num
fato = num * (num - 1)
num -= 2
while num >= 1:
    fato = fato * num
    num -= 1
print('{}! é {}'.format(aux, fato))
