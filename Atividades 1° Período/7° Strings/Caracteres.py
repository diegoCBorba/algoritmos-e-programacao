while True:
    n = int(input())
    if n == 0:
        break
    palavra = input()
    l_letra = []
    l_imp = []
    for letra in palavra:
        l_letra.append(letra)
    for letras in range(n):
        l_imp.append(l_letra[letras])
    l_imp.reverse()
    print(''.join(l_imp))