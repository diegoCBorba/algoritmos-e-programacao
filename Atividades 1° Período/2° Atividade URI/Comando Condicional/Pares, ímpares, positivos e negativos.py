n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

# Número par
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
    n44 =  1
else:
    n44 = 0

if n5 % 2 == 0:
    n55 = 1
else:
    n55 = 0

# Número impar
if n1 % 2 == 0:
    n1i = 0
else:
    n1i = 1

if n2 % 2 == 0:
    n2i = 0
else:
    n2i = 1

if n3 % 2 == 0:
    n3i = 0
else:
    n3i = 1

if n4 % 2 == 0:
    n4i = 0
else:
    n4i = 1

if n5 % 2 == 0:
    n5i = 0
else:
    n5i = 1

# Número positivo
if n1 > 0:
    n1p = 1
else:
    n1p = 0

if n2 > 0:
    n2p = 1
else:
    n2p = 0

if n3 > 0:
    n3p = 1
else:
    n3p = 0

if n4 > 0:
    n4p = 1
else:
    n4p = 0

if n5 > 0:
    n5p = 1
else:
    n5p = 0

# Números negativo
if n1 < 0:
    n1n = 1
else:
    n1n = 0

if n2 < 0:
    n2n = 1
else:
    n2n = 0

if n3 < 0:
    n3n = 1
else:
    n3n = 0

if n4 < 0:
    n4n = 1
else:
    n4n = 0

if n5 < 0:
    n5n = 1
else:
    n5n = 0


total = n11 + n22 + n33 + n44 + n55
print("{} valor(es) par(es)".format(total))
totali = n1i + n2i + n3i + n4i + n5i
print("{} valor(es) impar(es)".format(totali))
totalp = n1p + n2p + n3p + n4p + n5p
print("{} valor(es) positivo(s)".format(totalp))
totaln = n1n + n2n + n3n + n4n + n5n
print("{} valor(es) negativo(s)".format(totaln))