import math
angulo = int(input('Digite o ângulo: '))
cos = math.cos(angulo)
sen = math.sin(angulo)
tan = math.tan(angulo)
print('Baseado no ângulo {}º\nO valor do seno é {:.2f}!\nO coseno é {:.2f}!\nO tangente é {:.2f}!'.format(angulo, sen, cos, tan))