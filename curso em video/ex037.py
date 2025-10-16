num = int(input('Digite um número qualquer: '))
print('''Escolha uma das base de conversao:''')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
base = int(input('Digite sua base de conversao: '))

if base == 1:
    print('Convertido para BINARIO')
    print('A base binária do número {} é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('Convertido para OCTAL')
    print('A base octal para o número {} é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('Convertido para HEXADECIMAL')
    print('A base hexadecimal para o número {} é {}'.format(num, hex(num)[2:]))
