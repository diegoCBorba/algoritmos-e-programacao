palavra = input().upper()
l_letra = []
[l_letra.append(i) for i in palavra]


for repeticao in range(1 + len(l_letra)):
    for vezes in range(repeticao):
        if vezes == repeticao - 1:
            print(l_letra[vezes])
        else:
            print(l_letra[vezes], end='')
