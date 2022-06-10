nome = input('Entre com o seu nome completo: ')
nome = nome.lower()
nome = nome.find('silva')
if nome != -1 :
    print('Voce possui o nome \"Silva\"')
else:
    print('Voce não possui o nome \"Silva\"')