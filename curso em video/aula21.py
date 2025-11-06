def fatorial(num=1):
    f =1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número para calcular seu fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

