n = int(input())

letras = []

for i in range(n):
    letras.append('')

for i in range(n):
    indice, letra = input().split()
    letras[int(indice)-1] = letra

print(''.join(letras))