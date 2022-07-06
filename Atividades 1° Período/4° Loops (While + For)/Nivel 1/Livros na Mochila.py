count = 0
peso_total = 0

while True:
    peso_L = int(input())

    if peso_total + peso_L <= 18:
        count += 1

    peso_total += peso_L

    if peso_total >= 18:
        break

print(count)
