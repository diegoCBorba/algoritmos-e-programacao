n_de_sudoku = int(input())
n_instancia = 0

for qnt_jogos in range(n_de_sudoku):
    n_instancia += 1
    vdd_ou_falso = True
    matriz_sudoku = []
    for linha in range(9):
        linhas = list(map(int, input().split()))
        matriz_sudoku.append(linhas)
    for linha in range(len(matriz_sudoku)):
        for coluna in range(len(matriz_sudoku)):
            for coluna_linha in range(len(matriz_sudoku)):
                if coluna != coluna_linha:
                    if matriz_sudoku[linha][coluna] == matriz_sudoku[linha][coluna_linha]:
                        vdd_ou_falso = False
                if linha != coluna_linha:
                    if matriz_sudoku[linha][coluna] == matriz_sudoku[coluna_linha][coluna]:
                        vdd_ou_falso = False

    if n_instancia == n_de_sudoku:
        if vdd_ou_falso:
            print(f'Instancia {n_instancia}')
            print('SIM')
        else:
            print(f'Instancia {n_instancia}')
            print('NAO')
    else:
        if vdd_ou_falso:
            print(f'Instancia {n_instancia}')
            print('SIM')
            print()
        else:
            print(f'Instancia {n_instancia}')
            print('NAO')
            print()