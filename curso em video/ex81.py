lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp not in 'SsNn':
        resp = input('Resposta Inválida. Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
print('Você digitou um total de {} números.'.format(len(lista)))
lista.sort(reverse=True)
print('Os valores em ordem decrescente são: {}'.format(lista))
if 5 in lista:
        print('O valor 5 faz parte da lista.')
else:
        print('O valor 5 não foi encontrado na lista.')