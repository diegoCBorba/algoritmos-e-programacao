crescente = []
a, b, c = map(float, input().split())
crescente.extend([a, b, c])
crescente.sort()
c, b, a = crescente

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    if a**2 > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b != c:
        print("TRIANGULO ISOSCELES")
    if a != b == c:
        print("TRIANGULO ISOSCELES")
    if a == c != b:
        print("TRIANGULO ISOSCELES")

"""
a, b, c = map(float, input().split())
maior = a
aux = 0

if b > maior:
    aux = b
    b = maior
    a = aux
    maior = a
if c > maior:
    aux = c
    c = maior
    a = aux
    
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    if a**2 > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b != c:
        print("TRIANGULO ISOSCELES")
    if a != b == c:
        print("TRIANGULO ISOSCELES")
    if a == c != b:
        print("TRIANGULO ISOSCELES")

"""




