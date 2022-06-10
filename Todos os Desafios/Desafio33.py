n1 = int(input('Entre com um inteiro: '))
n2 = int(input('Entre com outro inteiro: '))
n3 = int(input('Entre com mais um inteiro : '))
if n1 > n2 and n2 > n3:
    print('1° {}, 2° {}, 3°{}'.format(n1,n2,n3))
elif n1 > n2 and n3 > n2 :
    print('1° {}, 2° {}, 3°{}'.format(n1, n3, n2))
elif n1 < n2 and n1 > n3 :
    print('1° {}, 2° {}, 3°{}'.format(n2, n1, n3))
