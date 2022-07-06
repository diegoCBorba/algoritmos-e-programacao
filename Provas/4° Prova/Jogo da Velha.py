def verifica_jogo(matriz):
    # Verificação das linhas
    for linhas0 in matriz:
        if linhas0 == ['X', 'X', 'X']:
            return 'X'
        elif linhas0 == ['O', 'O', '0']:
            return 'O'

    # Verificação das colunas
    for linhas0 in range(len(matriz)):
        armazena_coluna = []
        for colunas in range(len(matriz)):
            armazena_coluna.append(matriz[colunas][linhas0])
        if armazena_coluna == ['X', 'X', 'X']:
            return 'X'
        elif armazena_coluna == ['O', 'O', 'O']:
            return 'O'

    # Verificação da diagonal principal
    armazena_diagonal = []
    for linhas0 in range(len(matriz)):
        for colunas in range(len(matriz)):
            if linhas0 == colunas:
                armazena_diagonal.append(matriz[colunas][linhas0])
    if armazena_diagonal == ['X', 'X', 'X']:
        return 'X'
    elif armazena_diagonal == ['O', 'O', 'O']:
        return 'O'

    # Verificação da diagonal secundária
    armazena_diagonal_secundaria = []
    for linhas0 in range(len(matriz)):
        for colunas in range(len(matriz)):
            if linhas0 + colunas == 2:
                armazena_diagonal_secundaria.append(matriz[colunas][linhas0])
    if armazena_diagonal_secundaria == ['X', 'X', 'X']:
        return 'X'
    elif armazena_diagonal_secundaria == ['O', 'O', 'O']:
        return 'O'

    return 'Empate ou em andamento'


while True:
    matriz_jogo = []
    for linhas in range(3):
        linha = input().split()
        if linha == ['sair']:
            exit(0)
        matriz_jogo.append(linha)
    print(verifica_jogo(matriz_jogo))