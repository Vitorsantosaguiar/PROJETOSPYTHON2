print('='*20)
print('10 termos de uma PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 1
atual = termo

while contador <= 10:
    print(f'{atual}', end=' ')
    atual += razao
    contador += 1

print('\nFIM')
