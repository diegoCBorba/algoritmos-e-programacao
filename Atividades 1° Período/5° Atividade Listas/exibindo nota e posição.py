"""
n = int(input())
if n == 0:
    print('Numero de notas invalido.')
    exit(0)

media = 0
lista = []

for i in range(n):
    nota = float(input())
    lista.append(nota)
    media += nota

for x in range(n):
    print('Nota {}: {}'.format(x + 1, lista[x]))

media_final = media/n
print('Media: {:.2f}'.format(media_final))
"""

n = int(input())
if n == 0:
    print('Numero de notas invalido.')
    exit(0)

media = 0
lista = []

for i in range(n):
    nota = float(input())
    print('Nota {}: {}'.format(i + 1, nota))
    media += nota

media_final = media/n
print('Media: {:.2f}'.format(media_final))