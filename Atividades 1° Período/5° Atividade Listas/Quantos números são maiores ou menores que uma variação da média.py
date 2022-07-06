n_notas = int(input())
notas = []
acima_media = 0
abaixo_media = 0

for i in range(n_notas):
    nota = int(input())
    notas.append(nota)

media = sum(notas)/n_notas
for j in notas:
    if j >= (media*1.1):
        acima_media += 1
    if j <= (media*0.9):
        abaixo_media += 1

print("{:.2f}".format(media))
print(acima_media)
print(abaixo_media)