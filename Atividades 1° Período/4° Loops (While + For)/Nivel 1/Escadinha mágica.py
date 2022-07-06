n = int(input())
soma_sequencia = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == i:
            print(j)
        else:
            print(j, end=' ')
