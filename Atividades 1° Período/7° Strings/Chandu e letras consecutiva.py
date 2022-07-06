n = int(input())

for i in range(n):
    palavra = input()
    l_letras = []
    l_atual = ''
    for letras in palavra:
        l_anterior = l_atual
        l_atual = letras
        if l_anterior != l_atual:
            l_letras.append(letras)

    print(''.join(l_letras))