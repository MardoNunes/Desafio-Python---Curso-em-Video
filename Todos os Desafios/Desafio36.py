casa = float(input('Qula o valor da casa? \n'))
salario = float(input('Qual é o seu salário?\n '))
anos = int(input('Quantos anos deseja pagar a casa ?\n'))

parcela = casa / anos
limite = (30*salario) / 100

if parcela < limite:
    print('Empréstimo aprovado, boas compras!')
else:
    print('Empréstimo negado, limite de salario inferior!')