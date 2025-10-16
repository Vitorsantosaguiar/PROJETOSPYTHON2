total = totmil = menor = cont = barato = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Digite o valor do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('Fim Do Programa!')
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto com o menor preço foi o {barato} de R$ {menor:.2f}')