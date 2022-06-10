num = float(input('Entre com seu salario: $'))
if num > 1250.00:
    aumento = (10*num) / 100
    num=num+aumento
    print('Seu salario teve um aumento de 10%, agora ele é: ${}'.format(num))
else:
    aumento = (15*num) / 100
    num = num + aumento
    print('Seu salario teve um aumento de 15%, agora ele é: ${}'.format(num))