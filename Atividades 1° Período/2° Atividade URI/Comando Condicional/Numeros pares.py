n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

if n1 >= 0:
    n11 = 1
else:
    n11 = 0

if n2 >= 0:
    n22 = 1
else:
    n22 = 0

if n3 >= 0:
    n33 = 1

else:
    n33 = 0

if n4 >= 0:
    n44 = 1

else:
    n44 = 0

if n5 >= 0:
    n55 = 1

else:
    n55 = 0

if n6 >= 0:
    n66 = 1

else:
    n66 = 0

total = n11 + n22 + n33 + n44 + n55 + n66
print("{} valores positivos".format(total))