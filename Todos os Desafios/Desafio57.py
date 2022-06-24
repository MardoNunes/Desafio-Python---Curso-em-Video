#repetição até que seja digitado o sexo correto

sexo = 'J'
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Entre com seu sexo [M/F]: ')).upper()

if sexo == 'M':
    print('Voce é macho, congratulation')
elif sexo == 'F':
    print('Voce é femea, parabuais')