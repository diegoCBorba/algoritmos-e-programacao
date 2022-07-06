l = int(input())
c = int(input())

m = []
for i in range(l):
    linha = []
    for j in range(c):
        elem = int(input())
        linha.append(elem)
    m.append(linha)

print(m)