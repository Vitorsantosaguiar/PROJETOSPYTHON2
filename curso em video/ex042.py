reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')

if reta1 == reta2 and reta3 == reta1:
    print('As retas formam um triângulo equilatero!!')

elif reta1 != reta2 and reta1 != reta3 and reta1 != reta2:
    print('As retas formam um triângulo escaleno!!')

elif reta1 == reta2 and reta1 != reta3:
    print('As retas formam um triângulo isóceles!!')