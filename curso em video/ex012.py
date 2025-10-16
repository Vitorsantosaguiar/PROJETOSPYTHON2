produto = float(input('Digite o valor do produto: '))
desconto = produto - (produto * 0.05)
print('O novo preço do produto com desconto é de R$ {:.2f}'.format(desconto))