n = int(input())

for vezes in range(n):
    l_palavra = []
    palavra = str(input())
    for i in palavra:
        l_palavra.append(i)
    l_palavra.reverse()
    print(''.join(l_palavra))