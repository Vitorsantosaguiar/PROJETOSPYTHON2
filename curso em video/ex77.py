tupla = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'grátis', 'estudar', 'praticar',)
print(tupla)
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')