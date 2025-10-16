n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O numero {} é maior que o numero {}'.format(n1, n2))
elif n1 < n2:
    print('O numero {} é maior que o numero {}'.format(n2, n1))
else:
    print('\033[1;31;40mOs dois numeros são iguais')