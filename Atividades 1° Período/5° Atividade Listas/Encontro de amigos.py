import sys

n = int(input())
d_amigos = list(map(int, input().split()))

pos = 0
maior = max(d_amigos)
menor_soma = sys.maxsize  # Maior valor inteiro

for i in range(1, maior+1):
    soma = 0
    for d in d_amigos:
        soma += abs(d - i)
    if soma < menor_soma:
        menor_soma = soma
        pos = i

print("{} {}".format(menor_soma, pos))
