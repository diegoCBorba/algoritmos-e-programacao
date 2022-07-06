import math

quadrado_anterior = 0
quadrado_atual = 0

while True:
    numero_impar = int(input())
    if not 0 <= numero_impar <= 10000:
        exit(0)
    if numero_impar == 0:
        exit(0)
    if numero_impar == 1:
        print('1 - 0')
    else:
        for i in range(1, numero_impar):
            quadrado_anterior = quadrado_atual
            quadrado_atual = i ** 2

            if (quadrado_atual - quadrado_anterior) == numero_impar:
                print("{} - {}".format(quadrado_atual, quadrado_anterior))