valor = float(input('Digite o valor da casa: '))
salario = float(input('Difite o seu salário: '))
anos = int(input('Quantos anos vai pagar a casa? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Emprestimo aprovado!')
    print('Valor da casa: R${:.2f}'.format(prestacao))
elif prestacao > minimo:
    print('Emprestimo reprovado!')
else:
    print('Emprestimo reprovado!')