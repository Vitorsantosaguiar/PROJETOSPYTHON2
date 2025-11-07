import moeda
# Programa principal
#Programa de conversão de moedas
valor = float(input("Digite o preço: R$ "))

aumentar = moeda.aumentar(valor, 10, True)
diminuir = moeda.diminuir(valor, 5, True)
dobro = moeda.dobro(valor, True)
metade = moeda.metade(valor, True)
print(f"Aumentando 10% de {moeda.moeda(valor)} temos {aumentar}")
print(f"Diminuindo 5% de {moeda.moeda(valor)} temos {diminuir}")
print(f"O dobro de {moeda.moeda(valor)} é {dobro}")
print(f"A metade de {moeda.moeda(valor)} é {metade}")
