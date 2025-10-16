frase = str(input('Digite uma frase: ')).strip()
print('quantidade de vezez: ',frase.upper().count('A'))
print('qual posição: ',frase.upper().find('A'))
print('qual posicão pela ultima vez: ',frase.upper().rfind('A'))