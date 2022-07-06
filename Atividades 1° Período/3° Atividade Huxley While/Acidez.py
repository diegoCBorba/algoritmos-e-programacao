while True:
    pH = float(input())

    if 0 <= pH < 7:
        print("ACIDA")

    if pH == 7:
        print("NEUTRA")

    if pH > 7:
        print("BASICA")

    if pH == -1:
        break
