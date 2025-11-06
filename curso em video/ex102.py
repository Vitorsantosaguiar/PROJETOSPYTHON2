def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.

    :param num: O número para calcular o fatorial.
    :param show: Se True, mostra o processo de cálculo.
    :return: O fatorial do número.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            if c > 1:
                print(f"{c} x ", end="")
            else:
                print(f"{c} = ", end="")
    return fat
# Programa Principal
n = int(input("Digite um número para calcular o fatorial: "))
print(fatorial(n, show=True))
print(fatorial(n))
