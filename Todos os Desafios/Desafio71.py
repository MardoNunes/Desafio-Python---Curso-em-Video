cont_onca = 0
contMico = 0
contArara = 0
contCent = 0
print('================')
print('CAIXA ELETRÔNICO')
print('================\n')

print('---------------------------------------------')
valor = int(input('Digite quanto você quer sacar: '))
print('---------------------------------------------\n')

while valor != 0:
    if valor >= 50:
        valor -= 50
        cont_onca += 1
    elif valor >= 20:
        valor -= 20
        contMico += 1
    elif valor >= 10:
        valor -= 10
        contArara += 1
    elif valor >= 1:
        valor -= 1
        contCent += 1

if valor == 0:
    print('Volte sempre!!')
else:
    print(f'Serão sacadas {cont_onca} de $50, {contMico} de $20, {contArara} de $10 e {contCent} moedas de $1 real !')





