def ajuda(com):    """Mostra a ajuda interativa do Python"""
    help(com)


def titulo(msg, cor):    """Mostra um título formatado"""
    tam = len(msg) + 4
    print(f'\033[{cor}m~' * tam)
    print(f'  {msg}')
    print('~' * tam + '\033[m')



# Programa Principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 44)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo("VOLTE SEMPRE!", 41)
