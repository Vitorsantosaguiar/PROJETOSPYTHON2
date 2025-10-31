from random import randint
from time import sleep
dado = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('==' * 20)
ranking = sorted(dado.items(), key=lambda item: item[1], reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('==' * 20)
