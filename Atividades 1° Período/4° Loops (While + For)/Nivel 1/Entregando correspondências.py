count = 0
total_n_cartas = 0
for i in range(7):
    n_cartas = int(input())
    total_n_cartas += n_cartas
    if n_cartas >= 100:
        count += 1

print(count)
print(total_n_cartas//7)
