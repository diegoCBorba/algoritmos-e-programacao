while True:
    n = int(input())
    if n == -1:
        break

    if n == 0 or n == 1:
        print(0)
    elif n == 2 or n == 3 or n == 5 or n == 7:
        print(1)
    elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print(1)
    else:
        print(0)