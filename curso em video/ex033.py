n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 > n3:
    print('O maior número é {} e o menor numero é {}'.format(n1, n3))
elif n2 > n1 and n2 > n3:
    print('O maior número é {} e o menor número é {}'.format(n2, n3))
else:
    print('O maior número é {} e o menor número é {}'.format(n1, n3))