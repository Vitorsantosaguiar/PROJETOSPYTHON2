n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
elif media < 7 or media == 5 or media <= 6.9:
    print('RECUPERACAO')