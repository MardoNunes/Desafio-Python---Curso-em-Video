from operator import truediv


cont = 0
soma = 0

while True:
    num = int(input('Entre com um numero (999 para parar!): '))
    if num == 999:
        break
    soma = soma + num
    cont += 1
print(f'Foram digitados {cont} numeros e soma entre eles foi {soma}')
