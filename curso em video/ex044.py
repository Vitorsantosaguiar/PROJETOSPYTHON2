valorproduto = float(input('Digite o valor do produto: '))
condicao = str(input('Digite a condição de pagamento: '))

if condicao == 'dinheiro':
    valorproduto = valorproduto - (valorproduto * 0.10)
    print('O valor a pagar pelo produto é de R$ {:.2f}'.format(valorproduto))
elif condicao == 'debito':
    valorproduto = valorproduto - (valorproduto * 0.05)
    print('O valor total a pagar pelo produto é de R$ {:.2f}'.format(valorproduto))
elif condicao == 'credito 2x':
    print('O valor total a pagar pelo produto é de R$ {:.2f}'.format(valorproduto))
elif condicao == 'credito 3x' or condicao == 'credito 4x' or condicao == 'credito 5x' or condicao == 'credito 6x' or condicao == 'credito 7x' or condicao == 'credito 8x' or condicao == 'credito 9x' or condicao == 'credito 10x' or condicao == 'credito 11x'  or condicao == 'credito 12x':
    valorproduto = valorproduto + (valorproduto * 0.20)
    print('O valor total a pagar pelo produto é de R$ {:.2f}'.format(valorproduto))