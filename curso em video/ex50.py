soma = 0
cont = 0
for c in range(0, 6):
    n1 = int(input('Digite um valor: '))
    if n1 % 2 == 0:
        cont = cont + 1
        soma = soma + n1
print('A soma dos {} valores é {}'.format(cont, soma))
