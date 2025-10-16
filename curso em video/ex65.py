resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {:.2f}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
print('FIM DA PROGRAMA')