galera = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    galera.append(pessoa.copy())
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
soma = 0
for p in galera:
    soma += p['idade']
print(f'B) A soma das idades é {soma}.')
media = soma / len(galera) if galera else 0
print(f'C) A média de idade é {media:.2f} anos.')
print('D) As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('E) Lista de pessoas acima da média:')
for p in galera:
    if p['idade'] > media:
        print(f'   {p["nome"]} com {p["idade"]} anos.')