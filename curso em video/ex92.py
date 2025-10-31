nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = 2024 - ano
carteira = int(input('Carteira de trabalho (0 não tem): '))
pessoa = {'nome': nome, 'idade': idade}
if carteira != 0:
    ano_contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    pessoa['carteira'] = carteira
    pessoa['ano de contratação'] = ano_contratacao
    pessoa['salário'] = salario
    pessoa['aposentadoria'] = idade + ((ano_contratacao + 35) - 2024)
print('-=' * 20)
for k, v in pessoa.items():
    print(f'  - {k} é igual a {v}')
print('-=' * 20)
