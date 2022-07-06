m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Elementos na diagonal")
print()
for i in range(len(m)):
    for j in range(len(m[i])):
        if i == j:
            if j == len(m[i]) - 1:
                print(m[i][j], end='')
            else:
                print(m[i][j], end=' ')
        else:
            print('_', end=' ')
    print()

print()
print("Elementos acima da diagonal")
print()
for i in range(len(m)):
    for j in range(len(m[i])):
        if i < j:
            if j == len(m[i]) - 1:
                print(m[i][j], end='')
            else:
                print(m[i][j], end=' ')
        else:
            print('_', end=' ')
    print()

print()
print("Elementos abaixo da diagonal")
print()
for i in range(len(m)):
    for j in range(len(m[i])):
        if i > j:
            if j == len(m[i]) - 1:
                print(m[i][j], end='')
            else:
                print(m[i][j], end=' ')
        else:
            print('_', end=' ')
    print()