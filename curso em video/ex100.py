numeros = list()
def sorteia():
    from random import randint
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print('Sorteando 5 valores da lista:', end=' ')
    for n in numeros:
        print(f'{n}', end=' ')
    print('PRONTO!')

def somaPar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos {s}')

# Programa principal
sorteia()
somaPar()