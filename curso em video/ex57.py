sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
print('Fim')