m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(m)):
    for j in range(len(m[i])):
        if j == len(m[i]) - 1:
            print(m[i][j])
        else:
            print(m[i][j], end= ' ')