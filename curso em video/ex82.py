lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    listapar = []
    listaimpar = []
    for n in lista:
        if n % 2 == 0:
            listapar.append(n)
        else:
            listaimpar.append(n)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
print('Fim do programa.')
print('-=' * 30)