n = int(input())

for i in range(n):
    palavra = input().upper()
    l_palavra = []
    for pal in palavra:
        if pal != ' ':
            l_palavra.append(pal)
    l_palavra_reverse = l_palavra.copy()
    l_palavra_reverse.reverse()
    if l_palavra == l_palavra_reverse:
        print('SIM')
    else:
        print('NAO')