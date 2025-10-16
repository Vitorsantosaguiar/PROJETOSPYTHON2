produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30)

print('-=' * 15)
print(f'{"Tabela de Preços":^30}')
print('-=' * 15)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<25} R$ {produtos[i+1]:>7.2f}')