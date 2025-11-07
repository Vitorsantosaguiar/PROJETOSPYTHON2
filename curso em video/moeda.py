def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Função para aumentar o valor de um preço em uma determinada taxa.
    :param preco: Preço original.
    :param taxa: Percentual de aumento.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: Valor aumentado, formatado se solicitado.
    """
    valor_aumentado = preco + (preco * taxa / 100)
    return valor_aumentado if not formato else moeda(valor_aumentado)

def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Função para diminuir o valor de um preço em uma determinada taxa.
    :param preco: Preço original.
    :param taxa: Percentual de diminuição.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: Valor diminuído, formatado se solicitado.
    """
    valor_diminuido = preco - (preco * taxa / 100)
    return valor_diminuido if not formato else moeda(valor_diminuido)

def dobro(preco=0, formato=False):
    """
    -> Função para calcular o dobro de um preço.
    :param preco: Preço original.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: Dobro do valor, formatado se solicitado.
    """
    valor_dobro = preco * 2
    return valor_dobro if not formato else moeda(valor_dobro)

def metade(preco=0, formato=False):
    """
    -> Função para calcular a metade de um preço.
    :param preco: Preço original.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: Metade do valor, formatado se solicitado.
    """
    valor_metade = preco / 2
    return valor_metade if not formato else moeda(valor_metade)
