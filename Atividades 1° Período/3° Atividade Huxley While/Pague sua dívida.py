totalD = int(input())
mDivida = int(input())

while True:
    print("(antes) {}".format(totalD))
    totalD = totalD - mDivida

    if totalD <= 0:
        print("(depois) 0")
        break

    elif totalD > 0:
        print("(depois) {}".format(totalD))