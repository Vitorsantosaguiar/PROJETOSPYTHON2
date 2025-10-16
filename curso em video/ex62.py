print('='*20)
print('10 termos de uma PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 1
atual = termo
total_termos = 10  # inicializa com 10 termos

while total_termos != 0:
    exibidos = 0
    while exibidos < total_termos:
        print(f'{atual}', end=' ')
        atual += razao
        exibidos += 1
        contador += 1
    print()  # pular linha após exibir os termos
    total_termos = int(input('Quantos termos a mais você quer mostrar? (0 para sair) '))

print('FIM DA PROGRESSÃO')