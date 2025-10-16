frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('A frase {} é um palíndromo'.format(frase))
else:
    print('A frase {} não é um palíndromo'.format(frase))
