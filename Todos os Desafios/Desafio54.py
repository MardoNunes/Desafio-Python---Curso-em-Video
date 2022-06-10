
ano = 2022
for i in range(0, 7):
    num = int(input('Entre com seu ano de nascimento: '))
    if ano - num > 18:
        print('Parabénss, você atingiu a maioridade, ja pode ser presso amigão!! \n{}Avaliando idade em 2022!{}'.format('\033[31m', '\033[m'))
    else:
        print('Você ainda é menor de idade, rlx o facho! \n {}Avaliando idade em 2022!!{}'.format('\033[32m', '\033[m'))