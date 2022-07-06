lista = []
count = 0

for i in range(10):
    n = int(input())
    lista.append(n)

x = int(input())

for j in lista:
    if x == j:
        count += 1

