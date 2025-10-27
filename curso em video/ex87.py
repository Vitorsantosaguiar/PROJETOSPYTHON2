matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 20)
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos valores pares é {soma}.')
soma3 = 0
for l in range(0, 3):
    soma3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma3}.')
maior = matriz[1][0]
for l in range(0, 3):
    if matriz[l][0] > maior:
        maior = matriz[l][0]
print(f'O maior valor da primeira coluna é {maior}.')
print('-=' * 20)