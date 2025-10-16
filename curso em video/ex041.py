idade = int(input('Digite a sua idade para saber suacategoria: '))
if idade < 10:
    print('Sua idade é menor que {} anos, sua categoria é MIRIM'.format(idade))

elif idade <= 14:
    print('Sua idade é {}, então sua categoria é INFANTIL'.format(idade))

elif idade > 14 and idade <= 19:
    print('Sua idade é {}, então sua categoria é JUNIOR'.format(idade))

elif idade == 20:
    print('Sua idade é {}, então sua categoria é SÊNIOR'.format(idade))

else:
    print('Sua idade é maior do que 20 anos, emtão sua categoria é MASTER'.format(idade))