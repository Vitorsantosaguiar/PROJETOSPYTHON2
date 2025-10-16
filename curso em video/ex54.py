from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
cont = 0
for c in range(1, 8):
    cont += 1
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cont)))
    if atual - nasc < 21:
        totmenor += 1
    else:
        totmaior += 1
print('Temos {} pessoas maiores de idade'.format(totmaior))
print('Temos {} pessoas menores de idade'.format(totmenor))
