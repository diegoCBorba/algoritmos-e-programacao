soma = 0
linhas = []
soma_diagonal = 0
for linha in range(3):
    for colunas in range(3):
        n = int(input())
        linhas.append(n)
        soma += n
        if linha == colunas:
            soma_diagonal += n

if max(linhas) > 1:
    print('{:.2f} {:.0f} 1 {:.0f}'.format(soma/9, max(linhas), soma_diagonal))
elif max(linhas) < 0:
    print('{:.2f} {:.0f} -1 {:.0f}'.format(soma/9, max(linhas), soma_diagonal))
else:
    print('{:.2f} {:.0f} 0 {:.0f}'.format(soma/9, max(linhas), soma_diagonal))

