peso_max = 560
total_peso = 0
count = 0

while True:
    peso = int(input())
    total_peso += peso
    if peso != 0:
        count += 1
    if count >= 7 or peso == 0 or total_peso >= peso_max:
        break

print(count)
print("{:.1f}".format(total_peso))
