lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    if num in lista:
        print('Valor duplicado! Não será adicionado à lista.')
        lista.pop()  # Remove o último valor adicionado (duplicado)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort()
print(f'Os valores em ordem crescente são {lista}.')
menor = lista[0]

