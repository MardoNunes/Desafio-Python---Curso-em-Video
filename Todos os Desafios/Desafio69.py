
contIdade = 0
contHomem = 0
contMulher = 0
while True:
    idade = int(input('Entre com a idade: '))
    sexo = str(input('Entre com o sexo[F/M]: ')).upper()

    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if (sexo == 'F') and (idade <= 20):
        contMulher += 1

    keep = str(input('Você deseja continuar?[S/N]\n')).upper()
    if keep == 'N':
        break     

print(f'Há {contIdade} pessoas com mais de 18 anos!')
print(f'Há {contHomem} homens!')
print(f'Há {contMulher} mulheres com menos de 20 anos!')





