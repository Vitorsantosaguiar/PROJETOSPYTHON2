def maior(*num):
    from time import sleep
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    maior = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)
# Programa principal
maior(2, 3, 5, 6, 9)