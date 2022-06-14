soma = 0
idadeMaior = 0
nomeMaior = ''
cont = 0
for i in range(1, 5):
    print('----- {}º PESSOA ------'.format(i))
    nome = str(input('Qual é seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: '))

    soma = soma + idade

    if i == 1 and sexo in 'Mm':
        idadeMaior = idade
        nomeMaior = nome
    if sexo in 'Mm' and idade > idadeMaior:
        idadeMaior = idade
        nomeMaior = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1

mediaIdade = soma / 4
print('A média de idades é {}\n'.format(mediaIdade),
      'O homem mais velho tem {} anos e se chama {}\n'.format(idadeMaior, nomeMaior),
      'Há {} mulheres com menos de 20 anos!'.format(cont))
