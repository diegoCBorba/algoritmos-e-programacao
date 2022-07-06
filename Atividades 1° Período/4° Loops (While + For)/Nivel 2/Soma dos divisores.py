soma_divisores = 0
soma_anterior = 0

for i in range(5):
    n = int(input())
    soma_divisores = 0
    for j in range(1, n+1):
        if n % j == 0:
            soma_divisores += j
        if soma_divisores > soma_anterior:
            maior_soma = n
            soma_anterior = soma_divisores

print(maior_soma)