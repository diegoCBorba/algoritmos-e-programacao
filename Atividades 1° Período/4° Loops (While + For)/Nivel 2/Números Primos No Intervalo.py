n1 = int(input())
n2 = int(input())

maior = n2
aux = 0

if n1 > maior:
    aux = n1
    n1 = maior
    n2 = aux
    maior = n2

for i in range(n2, n1 - 1, -1):
    if not i == 1:
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i)
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i)
