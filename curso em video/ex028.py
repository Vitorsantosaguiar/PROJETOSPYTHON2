from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Escolha um numero entre 0 e 5: ')) # o jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você ganhou!')
else:
    print('Eu ganhei! Eu pensei no numero {}'.format(computador))