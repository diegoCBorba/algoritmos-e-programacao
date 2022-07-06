n1 = int(input())
n2 = int(input())
soma_total = 0

maior = n1
aux = 0

if n1 > n2:
    aux = n2
    n2 = maior
    n1 = aux

if n1 < 0:
    n1 = 0

for i in range(n1, n2 + 1):
    soma_total += i

print(soma_total)
