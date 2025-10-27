pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]} pesa {p[1]}kg e é uma pessoa pesada.')
for p in pessoas:
    if p[1] < 100:
        print(f'{p[0]} pesa {p[1]}kg e é uma pessoa leve.')
print('<< ENCERRADO >>')
print('-=' * 30)

