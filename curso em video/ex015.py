d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (km * 0.15) + (d * 60)
print('O valor a pagar pelo aluguel é de R${:.2f}'.format(valor))