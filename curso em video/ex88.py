#Programa de MEGA SENA
from random import sample
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0, quantidade):
    numeros = sample(range(1, 61), 6)
    numeros.sort()
    print(f'Jogo {j + 1}: ', end='')
    print(*numeros)
print('BOA SORTE!')
#Programa de MEGA SENA