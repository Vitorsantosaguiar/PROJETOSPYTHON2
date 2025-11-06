def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    
    Parâmetros:
    n : float
        Notas dos alunos.
    sit : bool, opcional
        Se True, inclui a situação do aluno na análise.
        
    Retorna:
    dict
        Dicionário com a quantidade de notas, maior nota, menor nota,
        média das notas e, se solicitado, a situação do aluno.
    """
    resultado = {}
    resultado['total'] = len(n)
    resultado['maior'] = max(n) if n else 0
    resultado['menor'] = min(n) if n else 0
    resultado['média'] = sum(n) / len(n) if n else 0
    
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'Boa'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'Razoável'
        else:
            resultado['situação'] = 'Ruim'
    
    return resultado
# Programa Principal
resp = notas(5.5, 2.5, 9.0, sit=True)
print(resp)
