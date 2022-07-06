notas_alunos = []
nomes_alunos = []
nome_notas_dist = {}
notas_dist = []
count = 0

for i in range(5):
    notas = float(input())
    nome = str(input())
    nome.capitalize()
    notas_alunos.append(notas)
    nomes_alunos.append(nome)

media = sum(notas_alunos)/5

for j in range(5):
    if notas_alunos[j] <= media:
        nome_notas_dist[nomes_alunos[j]] = media - notas_alunos[j]
        notas_dist.append(media - notas_alunos[j])
    else:
        nome_notas_dist[nomes_alunos[j]] = notas_alunos[j] - media
        notas_dist.append(notas_alunos[j] - media)

nota_dist_max = max(notas_dist)

notas_alunos.sort()
notas_alunos.reverse()

for k in range(len(notas_alunos)):
    if k == len(notas_alunos)-1:
        print("{:.2f}".format(notas_alunos[k]))
    else:
        print("{:.2f}".format(notas_alunos[k]), end=' ')

print("{:.2f}".format(media))

for p in range(len(notas_dist)):
    if p == len(notas_dist)-1:
        print("{:.2f}".format(notas_dist[p]))
    else:
        print("{:.2f}".format(notas_dist[p]), end=' ')

for nome, dist in nome_notas_dist.items():
    if nota_dist_max == dist:
        print(nome.capitalize())
        print(count)
        break
    count += 1
