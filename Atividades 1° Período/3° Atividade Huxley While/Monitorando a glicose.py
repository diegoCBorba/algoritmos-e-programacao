count = 0
soma_glicose = 0

while True:
    glicose = int(input())
    soma_glicose = soma_glicose + glicose
    count += 1

    if glicose == 0:
        total = soma_glicose / (count - 1)

        if total < 110:
            print("Glicose Normal")

        elif total >= 200:
            print("Glicose Muito Alta")

        else:
            print("Glicose Alterada")
        break
