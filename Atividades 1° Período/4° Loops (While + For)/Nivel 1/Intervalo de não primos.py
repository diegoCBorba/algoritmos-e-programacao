n = int(input())
count = 0

if n == 0:
    exit(0)

print(1, end=' ')
for i in range(1, n + 1):
    if (i != 2) and (i != 3) and (i != 5) and (i != 7) and (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
        print(i, end=' ')
