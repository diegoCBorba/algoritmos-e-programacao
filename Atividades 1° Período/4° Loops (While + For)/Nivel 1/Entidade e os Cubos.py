num_cubos = int(input())
contador_andares = 0
acumulador1 = 1
acumulador2 = 2

while num_cubos > 0:
    num_cubos -= acumulador1

    if num_cubos >= 0:
        contador_andares += 1

    acumulador1 += acumulador2
    acumulador2 += 1

print(contador_andares)
