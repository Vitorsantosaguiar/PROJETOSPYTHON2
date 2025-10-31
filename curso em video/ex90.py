for c in range(0, 1):
    nome = str(input('Nome: '))
    media = float(input(f'Média de {nome}: '))
    aluno = {'nome': nome, 'média': media}
    if media >= 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'
    print('-=' * 20)
    for k, v in aluno.items():
        print(f'  - {k} é igual a {v}')
print('-=' * 20)