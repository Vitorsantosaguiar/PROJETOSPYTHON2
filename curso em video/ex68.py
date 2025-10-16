from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpiI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador jogou {computador} o total {total} ', end = '')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if computador % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Voce venceu {v} vezes')
