n_bandeja = int(input())
count_copos = 0

for i in range(n_bandeja):
    lata, copo = map(int, input().split())
    if lata > copo:
        count_copos += copo

print(count_copos)
