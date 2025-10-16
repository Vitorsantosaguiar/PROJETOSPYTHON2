import random
from time import sleep
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('-=-'*20)
print('\033[1:33:0BEM VINDO AO JOKEMPO!!!')
print('-=-'*20)
jokempo = str(input('''Escolha entre:
 - PEDRA
 - PAPEL
 - TESOURA:\n '''))
print('PROCESSANDO...')
sleep(3)
if jokempo.upper() == computador:
    print('Eu escolhi {}, EMPATE!!'.format(computador))
elif jokempo.upper() == 'PAPEL' and computador == 'PEDRA':
    print('Eu joguei {}, você venceu!'.format(computador))
elif jokempo.upper() == 'PEDRA' and computador == 'TESOURA':
    print('Eu joguei {}, você venceu!'.format(computador))
elif jokempo.upper() == 'TESOURA' and computador == 'PAPEL':
    print('Eu joguei {}, você venceu!'.format(computador))
elif jokempo.upper() == 'PAPEL' and computador == 'TESOURA':
    print('Eu joguei {}, você perdeu!'.format(computador))
elif jokempo.upper() == 'PEDRA' and computador == 'PAPEL':
    print('Eu joguei {}, você perdeu!'.format(computador))
elif jokempo.upper() == 'TESOURA' and computador == 'PEDRA':
    print('Eu joguei {}, você perdeu!'.format(computador))