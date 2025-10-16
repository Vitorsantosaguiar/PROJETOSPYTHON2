vel = float(input('Digite a velocidade: '))
multa = (vel-80) * 7
if vel > 80:
    print('Limite de velocidade ultrapassado, você foi multado em {} reais'.format(multa))
else:
    print('Tenha um bom dia!')