listanumeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        listanumeros[0].append(n)
    else:
        listanumeros[1].append(n)
print(f'Lista de pares: {listanumeros[0]}')
print(f'Lista de ímpares: {listanumeros[1]}')