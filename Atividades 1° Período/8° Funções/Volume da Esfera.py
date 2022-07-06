r1 = float(input())
r2 = float(input())
r3 = float(input())

def VolumeEsfera(r):
    volume = (4 * 3.1416 * (r ** 3))/3
    return '{:.2f}'.format(volume)


print(VolumeEsfera(r1))
print(VolumeEsfera(r2))
print(VolumeEsfera(r3))