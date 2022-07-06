q_linha, q_coluna = map(int, input().split())
lista_matriz = []
menores_zero = 0
maiores_zero = 0
diagonal_principal = 0
diagonal_secundaria = 0

for linhas in range(q_linha):
    linha = []
    for colunas in range(q_coluna):
        elemento_coluna = int(input())
        linha.append(elemento_coluna)
        if elemento_coluna > 0:
            maiores_zero += 1
        elif elemento_coluna < 0:
            menores_zero += 1
    lista_matriz.append(linha)

print('Matriz formada:')
for linhas in range(len(lista_matriz)):
    for colunas in range(len(lista_matriz[linhas])):
        if colunas == (len(lista_matriz[linhas]) - 1):
            print(lista_matriz[linhas][colunas])
        else:
            print(lista_matriz[linhas][colunas], end=' ')

if q_linha != q_coluna:
    print('A diagonal principal e secundaria nao pode ser obtida.')
else:
    for linhas in range(len(lista_matriz)):
        for colunas in range(len(lista_matriz[linhas])):
            if linhas == colunas:
                diagonal_principal += lista_matriz[linhas][colunas]
            if ((linhas + 1) + (colunas + 1)) == q_coluna + 1:
                diagonal_secundaria += lista_matriz[linhas][colunas]

    print(f'A diagonal principal e secundaria tem valor(es) {diagonal_principal} e {diagonal_secundaria} respectivamente.')

print(f'A matriz possui {menores_zero} numero(s) menor(es) que zero.')
print(f'A matriz possui {maiores_zero} numero(s) maior(es) que zero.')