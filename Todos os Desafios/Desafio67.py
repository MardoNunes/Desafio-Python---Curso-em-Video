
cont = 0
while True:
    n = int(input('Entre com um inteior positivo: '))
    cont = 0
    if n < 0 :
        break
    else:
        while cont <= 10 :
            mult = cont * n
            print(f'{cont} x {n} = {mult}')
            cont += 1






