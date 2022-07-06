n = int(input())
n1 = 0
n2 = 0
n3 = 0
count = 0

if n == 0:
    print("Falso")
    exit(0)

for i in range(1, 100 + 1):
    n3 = n2
    n2 = n1
    n1 = i
    multiplicacao = n1 * n2 * n3
    if multiplicacao == n:
        print("{} * {} * {} = {}".format(n3, n2, n1, n))
        print("Verdadeiro")
    else:
        count += 1

if count == 100:
    print("Falso")