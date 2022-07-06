a, b, c = map(float, input().split())

conversaoA = a * 3.7854
conversaoB = b * 3.7854
conversaoC = c * 3.7854

if a <= 1 and b > 1 and c > 1:
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(c, conversaoC))

elif b <= 1 and a > 1 and c > 1:
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(c, conversaoC))

elif c <= 1 and b > 1 and a > 1:
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(c, conversaoC))

elif a <= 1 and b <= 1 and c > 1:
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(c, conversaoC))

elif a <= 1 and c <= 1 and b > 1:
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(c, conversaoC))

elif b <= 1 and c <= 1 and a > 1:
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(c, conversaoC))

elif a <= 1 and b <= 1 and c <= 1:
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÃO -> {:.2f} LITROS".format(c, conversaoC))

else:
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(a, conversaoA))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(b, conversaoB))
    print("{:.0f} GALÕES -> {:.2f} LITROS".format(c, conversaoC))

