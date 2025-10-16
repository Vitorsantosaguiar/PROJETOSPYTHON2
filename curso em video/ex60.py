# Calcula o fatorial de um número usando while

numero = int(input("Digite um número: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")
