while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input(f'Digite a primeira nota de {nome}: '))
    nota2 = float(input(f'Digite a segunda nota de {nome}: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
lista = []
lista.append([nome, (nota1 + nota2) / 2])
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[1]:>8.1f}') 
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'As notas de {lista[opc][0]} são {nota1} e {nota2}')
print('<<< VOLTE SEMPRE >>>')