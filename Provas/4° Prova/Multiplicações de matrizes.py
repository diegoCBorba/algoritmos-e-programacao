tipo_multiplicacao = input()

if tipo_multiplicacao == 'e':
    matriz_escalar = []
    escalar = int(input())
    tam_linha, tam_coluna = map(int, input().split())
    for linhas in range(tam_linha):
        linha = list(map(int, input().split()))
        matriz_escalar.append(linha)
    for linhas in range(tam_linha):
        for colunas in range(tam_coluna):
            matriz_escalar[linhas][colunas] = (matriz_escalar[linhas][colunas] * escalar)

    for linhas in range(len(matriz_escalar)):
        for colunas in range(len(matriz_escalar[linhas])):
            print(matriz_escalar[linhas][colunas], end=' ')
        print()

else:
    tam_linha1, tam_coluna1 = map(int, input().split())
    tam_linha2, tam_coluna2 = map(int, input().split())
    matriz1 = []
    matriz2 = []

    if tam_coluna1 != tam_linha2:
        print('erro')
        exit(0)
    else:
        for linhas in range(tam_linha1):
            linha = list(map(int, input().split()))
            matriz1.append(linha)

        for linhas in range(tam_linha2):
            linha = list(map(int, input().split()))
            matriz2.append(linha)

        matriz_final = []
        for linhas in range(tam_linha1):
            matriz_final.append([])
            for colunas in range(tam_coluna2):
                matriz_final[linhas].append(0)
                for elementos in range(tam_coluna1):
                    matriz_final[linhas][colunas] += matriz1[linhas][elementos] * matriz2[elementos][colunas]

        for linhas in range(len(matriz_final)):
            for colunas in range(len(matriz_final[linhas])):
                print(matriz_final[linhas][colunas], end=' ')
            print()
