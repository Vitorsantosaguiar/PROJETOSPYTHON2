lista = []
for v in range(0, 5):
    n = int(input('Digite um valor: '))
    lista.append(n)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ',end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')