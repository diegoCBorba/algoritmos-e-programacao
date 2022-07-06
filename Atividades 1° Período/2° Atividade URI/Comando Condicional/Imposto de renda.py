renda = float(input())

p1 = 0.08
p2 = 0.18
p3 = 0.28

if 0 <= renda <= 2000:
    print("Isento")

elif 2000 < renda <= 3000:
    sTotal = (renda - 2000) * p1
    print("R$ {:.2f}".format(sTotal))

elif 3000 < renda <= 4500:
    sTotal = (1000 * p1) + ((renda - 3000) * p2)
    print("R$ {:.2f}".format(sTotal))

elif renda > 4500:
    sTotal = ((1000 * p1) + (1500 * p2)) + (renda - 4500) * p3
    print("R$ {:.2f}".format(sTotal))



