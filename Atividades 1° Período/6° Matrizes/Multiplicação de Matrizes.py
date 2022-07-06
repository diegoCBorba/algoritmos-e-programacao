"""
- N representa a quantidade de linhas da matriz A.

- M representa a quantidade de colunas da matriz A e a quantidade de linhas da matriz B.

- O indica a quantidade de colunas da matriz B.

Note que só podemos multiplicar matrizes se o número de colunas da primeira for igual ao número de linhas segunda.
E que a nova matriz terá o tamanho de linhas da primeira e de colunas da segunda.
"""

n, m, o = map(int, input().split())
matriz_a = []
matriz_b = []

for linhas in range(n):
    num = list(map(int, input().split()))
    matriz_a.append(num)

for linhas in range(m):
    num = list(map(int, input().split()))
    matriz_b.append(num)

matriz_final = []
for linhas in range(n):
    matriz_final.append([])
    for colunas in range(o):
        matriz_final[linhas].append(0)
        for elementos in range(m):
            matriz_final[linhas][colunas] += matriz_a[linhas][elementos] * matriz_b[elementos][colunas]

for linhas in range(len(matriz_final)):
    for colunas in range(len(matriz_final[linhas])):
        if colunas == (len((matriz_final[linhas])) - 1):
            print(matriz_final[linhas][colunas])
        else:
            print(matriz_final[linhas][colunas], end=' ')
