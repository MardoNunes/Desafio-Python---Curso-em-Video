#Um menu de opções

n1 = int(input('Entre com um numero: '))
n2 = int(input('Entre com mais um numero: '))
aux = 0


while aux != 5:
    aux = int(input('O que voce deseja fazer com esse numero:\n [1]Somar\n [2]multiplicar\n [3]maior\n [4]Novo numero\n [5] sair do porgrama \n'))
    if aux == 1:
        soma = n1 + n2
        print('A soma desses dois numeros é {}\n'.format(soma))
    elif aux == 2:
        mult = n1 * n2
        print('A multiplicaçao entre esses dois numeros é {}\n'.format(mult))
    elif aux == 3:
        if n1 > n2:
            print('O maior é {}\n'.format(n1))
        else:
            print('O maior é {}\n'.format(n2))
    elif aux == 4:
        n1 = int(input('Beleza! novo numero saindo!!: \n'))
        n2 = int(input('Entre com o novo segundo numero parceiro: \n'))


