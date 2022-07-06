k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())
multiplo = 0

for dragao in range(1, d+1):
    if dragao % k == 0 or dragao % i == 0 or dragao % m == 0 or dragao % n == 0:
        multiplo += 1

print(multiplo)
