import math

rounds = int(input())

for i in range(rounds):
    v1, v2, d1, d2 = map(int, input().split(" "))

    while True:
        r1 = int(math.ceil(v2/d1))
        r2 = int(math.ceil(v1/d2))

        if r1 <= r2:
            print("Clodes")
            break

        else:
            d1 += 50

        v1 -= d2

        if v1 <= 0:
            print("Bezaliel")
            break
