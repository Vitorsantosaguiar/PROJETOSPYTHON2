import math
catop = float(input('Digite o cateto oposto: '))
catadj = float(input('Digite o cateto adjacente: '))
hip = math.hypot(catop, catadj)
print('O cumprimento da hipoternusa é: {:.2f}'.format(hip))