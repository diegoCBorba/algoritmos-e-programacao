soma_positivo = 0
linhas = []
soma_n_diagonal = 0
numeros_positivos = 0
for linha in range(3):
    for colunas in range(3):
        n = int(input())
        linhas.append(n)
        if n > 0:
            soma_positivo += n
            numeros_positivos += 1
        if linha != colunas:
            soma_n_diagonal += n

if min(linhas) % 2 == 0:
    print('{:.2f} {:.0f} 1 {:.0f}'.format(soma_positivo / numeros_positivos, min(linhas), soma_n_diagonal))
else:
    print('{:.2f} {:.0f} 0 {:.0f}'.format(soma_positivo / numeros_positivos, min(linhas), soma_n_diagonal))

