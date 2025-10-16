from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = 0
while jogador != computador:
    jogador = int(input('Escolha um numero entre 0 e 10: ')) # o jogador tenta adivinhar
    print('PROCESSANDO...')
    sleep(3)
    if jogador != computador:
        print('Numero errado!!')
print('Você acertou o numero {}'.format(jogador))