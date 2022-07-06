n_atletas = int(input())
qnt_saltos = int(input())
saltos_totais = []
nomes_participantes = []
medias_participantes = []

for nomes in range(n_atletas):
    nome = str(input())
    nomes_participantes.append(nome)
    saltos_totais.clear()
    for saltos in range(qnt_saltos):
        nota_salto = float(input())
        saltos_totais.append(nota_salto)

    if sum(saltos_totais) == 0 or qnt_saltos == 0:
        media = 0
    else:
        media = sum(saltos_totais)/qnt_saltos
    medias_participantes.append(media)

for i in range(len(nomes_participantes)):
    for j in range(i + 1):
        if nomes_participantes[j] > nomes_participantes[i]:
            inter = nomes_participantes[j]
            nomes_participantes[j] = nomes_participantes[i]
            nomes_participantes[i] = inter

            inter2 = medias_participantes[j]
            medias_participantes[j] = medias_participantes[i]
            medias_participantes[i] = inter2

for ordem in range(len(nomes_participantes)):
    print("{}: {:.1f}".format(nomes_participantes[ordem], medias_participantes[ordem]))


