while True:
    entrada = input()
    if entrada == "FIM":
        break
    a, b, c = map(float, entrada.split())

    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        print("INVALIDO")
    else:
        if a == b == c:
            print("EQUILATERO")
        elif a == b or b == c or a == c:
            print("ISOSCELES")
        elif a != b != c:
            print("ESCALENO")
