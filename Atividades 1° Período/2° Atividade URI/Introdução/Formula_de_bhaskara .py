a, b, c = map(float, input().split())

numb = -1 * b
div = 2 * a
dt = -4*a*c
quad = 2
raiz = 0.5
delta = (b**quad) + dt
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_de_delta = delta ** raiz
    r1 = (numb + raiz_de_delta)/div
    r2 = (numb - raiz_de_delta)/div
    print("R1 = {:.5f}\nR2 = {:.5f}".format(r1, r2))

