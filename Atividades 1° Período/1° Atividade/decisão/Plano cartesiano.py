x = float(input())
y = float(input())

if x > 0:
    if y > 0:
        print("Primeiro Quadrante")
    elif y < 0:
        print("Quarto Quadrante")
    elif y == 0:
        print("Sobre o eixo x")

elif x < 0:
    if y > 0:
        print("Segundo Quadrante")
    elif y < 0:
        print("Terceiro Quadrante")
    elif y == 0:
        print("Sobre o eixo x")

elif x == 0:
    if y > 0 or y < 0:
        print("Sobre o eixo y")
    elif y == 0:
        print("Sobre a origem")