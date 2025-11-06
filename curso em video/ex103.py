def ficha(nome='<desconhecido>', gols=0):
    """
    Função que retorna uma string formatada com o nome do jogador e a quantidade de gols.
    
    Parâmetros:
    nome (str): Nome do jogador. Padrão é '<desconhecido>'.
    gols (int): Quantidade de gols marcados. Padrão é 0.
    
    Retorna:
    str: String formatada com as informações do jogador.
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
