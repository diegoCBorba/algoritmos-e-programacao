x = int(input())
d = 0

copia_x = x
n = 0
mf = 0
freq = 0

for i in range(2, x+1):
    n = 0
    copia_x = x
    while copia_x % i == 0:
        copia_x = copia_x // i
        n += 1
    if n > freq:
        freq = n
        mf = i

print("mostFrequent: {}, frequency: {}".format(mf, freq))