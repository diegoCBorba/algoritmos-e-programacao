palavra = str(input())
l_palavra = []
for i in palavra:
    l_palavra.append(i)
l_palavra.reverse()
print(''.join(l_palavra))