p1 = float(input('Entre com a primeira nota: '))
p2 = float(input('Entre com a segunda nota: '))

media = (p1+p2) / 2

if media < 5 :
    print('REPROVADO')
elif (media == 5) and (media < 6.9):
    print('RECUPERAÇÂO')
else:
    print('APROVADO')






