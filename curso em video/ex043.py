peso = float(input('Digite o valor do seu peso: '))
altura = float(input('Digite o valor da altura: '))

imc = peso / (altura ** 2)
print('O seu IMC é de: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 1.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imd < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade mórbida')