import random
print('=========================')
print('vamos Jogar Par ou Impar!')
print('=========================')
cont = 0
while True:
    num = int(input('Digite um valor (de 0 à 10): '))
    esc = str(input('Voce escolhe Impar ou Par: ')).upper()
    pc = random.randint(0, 10)
    soma = num + pc
    if soma % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'IMPAR'
    if esc == pi:
        print(f'voce jogou {num} e o computador {pc}, {soma} é {pi} você ganhou!!')
        cont += 1
    else:
        print(f'voce jogou {num} e o computador {pc}, {soma} é {pi}, voce perdeu :(')
        break
print(f'Você ganhou {cont} vezes!! ')