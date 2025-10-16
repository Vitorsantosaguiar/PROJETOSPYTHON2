from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opção = 0
while opção != 5:
    print('PROCESSANDO...')
    sleep(1)
    print('Escolha uma das opções a seguir:')
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NUMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    opção = int(input('Digite a opção: '))
    if opção == 1:
        print('PROCESSANDO...')
        sleep(1)
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
        break
    elif opção == 2:
        print('PROCESSANDO...')
        sleep(1)
        multiplica = n1 * n2
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, multiplica))
        break
    elif opção == 3:
        print('PROCESSANDO...')
        sleep(1)
        if n1 > n2:
            maior = n1
            print('O maior número é {}'.format(maior))
        else:
            maior = n2
            print('O maior número é {}'.format(maior))
        break
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')

    sleep(1)

print('FIM DO PROGRAMA. Volte sempre!')
