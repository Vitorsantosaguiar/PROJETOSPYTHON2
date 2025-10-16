viagem = float(input('Digite a distância da viagem: '))
if viagem <= 200:
    viagem = 0.50 * viagem
else:
    viagem = 0.45 * viagem
print('Sua viagem custará R${:.2f}'.format(viagem))