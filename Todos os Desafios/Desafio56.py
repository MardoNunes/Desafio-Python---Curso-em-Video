#nome = input('Entre com seu nome: ')
#idade = int(input('Entre com sua idade: '))
#sexo = str(input('Entre com seu sexo: '))

soma = 0


for i in range(0, 5):
    nome = input('Entre com seu nome: ')
    idade = int(input('Entre com sua idade: '))
    sexo = str(input('Entre com seu sexo (Homem ou Mulher!): '))


    #tratamento das idades, meida entre as idades
    soma = soma + idade
    media = soma / 5

    #Qual o nome do homem mais velho
    if (sexo == 'homem') or (sexo == 'HOMEM') or (sexo == 'Homem'):
        idade_maiorH = idade
        if idade >= idade_maiorH:
            idade_maiorH = idade
            nome_maiorH = nome


    #Qual o nome da mulher mais velha
    if (sexo == 'mulher') or (sexo == 'Mulher') or (sexo == 'MULHER'):
        idade_maiorM = idade
        if idade >= idade_maiorM:
            idade_maiorM = idade
            nome_maiorM = nome

#Printar media de idade, nome do homem mais velhor, nome da mulher mais velha
print('Meida das idades: {}'.format(media))
print('Homem mais velhor: {} \n'
      'Mulher mais velha: {}'.format(nome_maiorH, nome_maiorM))