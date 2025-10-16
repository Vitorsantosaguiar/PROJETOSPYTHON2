nome  = str(input('Digite seu nome: '))
if nome == 'Paulo':
    print('Que nome bonito')
elif nome == 'Paulo' or nome == 'Vitor' or nome == 'maria' or nome == 'gustavo':
    print('Seu nome é popular no Brasil!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))