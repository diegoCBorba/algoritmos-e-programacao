n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

if n1 % 2 == 0:
    n11 = 1
else:
    n11 = 0

if n2 % 2 == 0:
    n22 = 1
else:
    n22 = 0

if n3 % 2 == 0:
    n33 = 1

else:
    n33 = 0

if n4 % 2 ==0:
    n44 = 1

else:
    n44 = 0

if n5 % 2 == 0:
    n55 = 1

else:
    n55 = 0

total = n11 + n22 + n33 + n44 + n55
print("{} valores pares".format(total))