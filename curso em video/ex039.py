from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(atual, idade, ano))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
