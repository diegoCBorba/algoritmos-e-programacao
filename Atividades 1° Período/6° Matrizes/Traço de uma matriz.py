matriz_quadratica = int(input())
if matriz_quadratica == 0:
    print('tr(A) = (0.00) = 0.00')
    exit(0)
matriz_principal = []
lista_valores_diagonal = []
saida = 'tr(A) ='
valor_total = 0

for linha in range(matriz_quadratica):
    linhas = list(map(float, input().split()))
    matriz_principal.append(linhas)

for i in range(len(matriz_principal)):
    valor_total += matriz_principal[i][i]
    lista_valores_diagonal.append(matriz_principal[i][i])

for i in range(len(lista_valores_diagonal)):
    if i == (matriz_quadratica - 1):
        saida += ' ({:.2f}) = {:.2f}'.format(lista_valores_diagonal[i], valor_total)
    else:
        saida += ' ({:.2f}) +'.format(lista_valores_diagonal[i])

print(saida)