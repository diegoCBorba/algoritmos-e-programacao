escala_de_medida = str(input())

if escala_de_medida == 'C':
    temperaturaC = float(input())
    temperaturaK = temperaturaC + 273.15
    temperaturaF = (temperaturaC*1.8) + 32
    if temperaturaC >= -273.15:
        print("{:.2f} F".format(temperaturaF))
        print("{:.2f} K".format(temperaturaK))

    else:
        print("Valor de temperatura abaixo do minimo")

if escala_de_medida == 'F':
    temperaturaF = float(input())
    temperaturaC = (temperaturaF - 32)/1.8
    temperaturaK = (temperaturaF - 32)*(5/9)+273.15
    if temperaturaF >= -459.67:
        print("{:.2f} C".format(temperaturaC))
        print("{:.2f} K".format(temperaturaK))

    else:
        print("Valor de temperatura abaixo do minimo")

if escala_de_medida == 'K':
    temperaturaK = float(input())
    temperaturaC = temperaturaK - 273.15
    temperaturaF = ((temperaturaK - 273.15) * 1.8) + 32
    if temperaturaK >= 0:
        print("{:.2f} C".format(temperaturaC))
        print("{:.2f} F".format(temperaturaF))

    else:
        print("Valor de temperatura abaixo do minimo")