#importa a biblioteca math com as funcões sqrt e floor(baixo)
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

#importa numeros aleatórios de 1 até 10
import random
num = random.randon(1, 10)
print(num)

#importa a biblioteca de emojis no programa(antes prercisa instalar o pacote)
import emoji
#imprime a mensagem ola mundo com o emoji de planeta
print(emoji.emojize('Olá mundo: earth_americas:', use_aliases=True))