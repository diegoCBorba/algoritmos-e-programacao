n = int(input())
anterior = 0
atual = 0
count = 0

for i in range(n):
    if i == count:
        print(atual)
    else:
        print(atual, end=' ')
    atual = anterior + atual
    anterior = atual - anterior
    count += 1
    if atual == 0:
        atual += 1

"""
anterior = 0
proximo = 0

while True:

    n = int(input())

    if n == 0:
        break

    else:
        anterior = 0
        proximo = 0

        for x in range(1, n + 1):
            if x == n:
                print(proximo)
            else:
                print(proximo, end=' ')

                proximo = proximo + anterior
                anterior = proximo - anterior

                if(proximo == 0):
                    proximo = proximo + 1
"""