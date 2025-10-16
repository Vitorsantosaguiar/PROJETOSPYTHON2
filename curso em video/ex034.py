salario = float(input('Digite o salario: '))
if salario > 1250:
    salario = salario * 0.10 + salario
    print('O seu salário atual é de R${:.2f}'.format(salario))
else:
    salario = salario * 0.15 + salario
    print('O seu salário é de R${:.2f}'.format(salario))