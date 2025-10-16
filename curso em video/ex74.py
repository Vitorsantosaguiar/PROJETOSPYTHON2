print('-=' * 15)
print('Gerador de Numeros Aleatórios')
print('-=' * 15)
from random import randint
from time import sleep
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='', flush=True)
    sleep(0.5)
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')