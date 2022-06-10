nome = input('Entre com o nome da sua cidade: ')
nome = nome.lower()
nome = nome.split()
if nome[0] == 'santo':
    print('Sua cidade começa com o nome \"Santo\"')
else:
    print('Sua cidade não começa com o nome \"Santo\"')