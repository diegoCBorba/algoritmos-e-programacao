while True:
    k = int(input())
    if k == 0:
        exit(0)
    matriz = []

    for linhas in range(4):
        linha = []
        for colunas in range(4):
            linha.append(0)
        matriz.append(linha)

    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[linhas])):
            n = int(input())
            if linhas == colunas:
                matriz[colunas][linhas] = (n * k)
            else:
                matriz[colunas][linhas] = n

    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[linhas])):
            print(matriz[linhas][colunas], end=' ')
        print()

