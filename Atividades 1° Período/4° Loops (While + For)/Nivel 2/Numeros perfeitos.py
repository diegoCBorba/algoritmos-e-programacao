n = int(input())

for i in range(1, n):
    soma_divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            soma_divisores += j

    if (i * 2) == soma_divisores:
        print(i)
