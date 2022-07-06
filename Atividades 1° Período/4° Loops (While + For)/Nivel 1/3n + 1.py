# Achar o ciclo de 1 número
n = int(input())
tam_ciclo = 1

while n > 1:
    print(n, end=" ")
    tam_ciclo += 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
print()
print(tam_ciclo)
# Achar os ciclos de 2 números
# Achar o maior ciclo dentre os ciclos de 2 números
# Para o programa quando não houver mais entradas

"""
n = int(input())
tam_ciclo = 1

while n > 1:
    tam_ciclo += n
    print(n, end=' ')
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1

print()
print(tam_ciclo)
"""