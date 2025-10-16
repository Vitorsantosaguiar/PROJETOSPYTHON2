tot18 = toth = totm20 = 0
while True:
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('Foram registradas {} mulheres menores de 20 anos.'.format(totm20))
print('Foram registradas {} pessoas com mais de 18 anos.'.format(tot18))
print('Foram registrados {} homens'.format(toth))