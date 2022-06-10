num = int(input('Entre com um numero: '))
maior = num
menor = num
for i in range(0, 4):
    num = int(input('Entre com um numero: '))
    if (num == maior) or (num > maior):
        maior = num
    elif (num == menor) or (num < menor):
        menor = num
print('O maior valor foi {}\n'
      'E o menor valor foi {}'.format(maior, menor))



