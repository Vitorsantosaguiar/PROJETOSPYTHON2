nome = str(input('Qual eé o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(media))
if media >= 7:
    print('A sua média foi boa! Parabéns')
else:
    print('Abaixo da media!! Estude mais!!')