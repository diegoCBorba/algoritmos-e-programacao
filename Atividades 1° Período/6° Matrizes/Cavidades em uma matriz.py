"""
linhas = int(input())
cols = int(input())

m = list()
for i in range(linhas):
    linha = list()
    for j in range(cols):
        elem = int(input())
        linha.append(elem)
    m.append(linha)

eh_cavidade_cima = 0
eh_cavidade_esq = 0
eh_cavidade_dir = 0
eh_cavidade_baixo = 0
cavidades = list()

for l in range(linhas):
    for c in range(cols):
        eh_cavidade_cima = 0
        eh_cavidade_esq = 0
        eh_cavidade_dir = 0
        for k in range(-1, 2): # Valores acima do elemento
            if (l-1 < 0 or c+k < 0 or c+k > cols-1): # verifica se está fora da da matriz
                eh_cavidade_cima += 1
            elif (l-1 >= 0 and c+k >= 0) and m[l-1][c+k] > m[l][c]: # Estando dentro da matriz verifica se o elemento analisado é menor
                eh_cavidade_cima += 1

        # Esquerda
        if c-1 < 0:
            eh_cavidade_esq += 1
        elif c-1 >= 0 and m[l][c-1] > m[l][c]:
            eh_cavidade_esq += 1

        # Direita
        if c+1 > cols-1:
            eh_cavidade_dir += 1
        elif c+1 <= cols-1 and m[l][c+1] > m[l][c]:
            eh_cavidade_dir += 1

        for k in range(-1, 2): # Valores abaixo do elemento
            if (l+1 > linhas-1 or c+k < 0 or c+k > cols-1): # verifica se está fora da da matriz
                eh_cavidade_cima += 1
            elif m[l+1][c+k] > m[l][c]: # Estando dentro da matriz verifica se o elemento analisado é menor
                eh_cavidade_cima += 1

        if eh_cavidade_cima + eh_cavidade_dir + eh_cavidade_esq == 8:
            cavidades.append((l, c))

print(cavidades)

q_linha = int(input())
q_colunas = int(input())
matriz = []
lista_final = []

for linhas in range(q_linha):
    linha = []
    for colunas in range(q_colunas):
        elementos = int(input())
        linha.append(elementos)
    matriz.append(linha)

for linhas in range(len(matriz)):
    for colunas in range(len(matriz[linhas])):
        eh_cavidade = True
        if linhas != (q_linha - 1):
            if matriz[linhas][colunas] > matriz[linhas - 1][colunas]:
                eh_cavidade = False
"""


