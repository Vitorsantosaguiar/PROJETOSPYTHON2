aproveitamento = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    aproveitamento.append(jogador)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
for i in aproveitamento:
    print(i)
print('-=' * 30)