ano = int(input('Entre com seu ano de nascimento: '))
idade = 2022 - ano

if (idade < 9) or (idade == 9):
    print('Nadador Mirim!')
elif (idade < 14) or (idade == 14):
    print('Nadador Infantil!')
elif (idade < 19) or (idade == 19):
    print('Nadador Junior')
elif (idade < 20) or (idade == 20):
    print('Nadador Sênior!')
else:
    print('Nadade Master')











