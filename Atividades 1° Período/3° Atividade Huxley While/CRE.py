semestre = int(input())
somaCH = 0
somaNota = 0

if semestre < 1 or semestre > 10:
    print("entrada invalida")
    exit(0)

while 0 < semestre <= 10:
    ch = int(input())
    nota = int(input())
    sitDisc = str(input())

    if (ch == 33 or ch == 50 or ch == 67 or ch == 83) and sitDisc == "A" or sitDisc == "R" or sitDisc == "RF":
        somaCH += ch
        somaNota += nota * ch

    semestre = int(input())

if somaCH == 0:
    print("entrada invalida")
if somaCH > 0:
    mediaPonderada = somaNota / somaCH
    print('{:.2f}'.format(mediaPonderada))
