while True:
    n = int(input('Digite um numero para ver a sua tabuada: '))
    if n < 0:
        print('Fim Do Programa')
        break
    print('-'*30)
    for c in range(0,11):
        print(f'{n} x {c} = {n*c}')
        print('-'*30)
