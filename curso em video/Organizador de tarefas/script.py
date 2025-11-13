tarefas = list()
while True:
    tarefa = str(input('Digite uma tarefa: '))
    tarefas.append(tarefa)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('TAREFAS:')
for i, t in enumerate(tarefas):
    print(f'{i + 1} - {t}')
print('-=' * 30)
print('Programa encerrado. Tenha um bom dia!')