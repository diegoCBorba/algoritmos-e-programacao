tipo_media = str(input())

if tipo_media == 'a':
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    mediaA = (nota1+nota2+nota3)/3
    print("{:.2f}".format(mediaA))
    if 70 <= mediaA <= 100:
        print("Aprovado")

    elif 0 <= mediaA <= 40:
        print("Reprovado")

    elif 40 < mediaA < 70:
        print("Final")

elif tipo_media == 'p':
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    peso1 = int(input())
    peso2 = int(input())
    peso3 = int(input())
    mediaP = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3))/(peso1 + peso2 + peso3)
    print("{:.2f}".format(mediaP))
    if 70 <= mediaP <= 100:
        print("Aprovado")

    elif 0 <= mediaP <= 40:
        print("Reprovado")

    elif 40 < mediaP < 70:
        print("Final")

elif tipo_media == 'h':
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    mediaH = 3/(1/nota1 + 1/nota2 + 1/nota3)
    print("{:.2f}".format(mediaH))
    if 70 <= mediaH <= 100:
        print("Aprovado")

    elif 0 <= mediaH <= 40:
        print("Reprovado")

    elif 40 < mediaH < 70:
        print("Final")


else:
    print("Escolha um tipo de media valida.")

