time = list()
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total_partidas):
    partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
time.append(jogador.copy())
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {total_partidas} partidas.')
for i, v in enumerate(partidas):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
