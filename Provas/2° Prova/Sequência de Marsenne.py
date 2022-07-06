"""
count = 0
while True:
    if count > 0:
        print()
    n = int(input())
    if n < 0:
        break
    if n == 1:
        print(1)
    else:
        for i in range(1, n):
            if i == 1:
                if n == 1:
                    print(1)
                else:
                    print("1", end=' ')
            else:
                if i == 2 or i == 3 or i == 5 or i == 7:
                    print("{}".format(i), end=' ')
                elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 11:
                    print("{}".format(i), end=' ')
        count += 1
"""

while True:
    print()
    m = int(input())
    if m < 0:
        break

    for x in range(m):
        cont1 = 0
        cont2 = 0
        for t in range(1, x + 1):
            if x % t == 0:
                cont1 += 1

        if cont1 == 2:
            mk = (2 ** x) - 1
            for w in range(1, mk + 1):
                if mk % w == 0:
                    cont2 += 1

        if x == 1 or cont2 == 2:
            print("{} ".format(x), end="")

