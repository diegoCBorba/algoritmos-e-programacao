gabarito = str(input())
gab_lista = []
for i in range(len(gabarito)):
    gab_lista.append(gabarito[i])
gab_lista_aluno = []
aluno_notas = {}
count_nota = 0
count_alunos = 0
notas = []

while True:
    count_nota = 0
    gab_lista_aluno.clear()
    nome_aluno = str(input())
    if nome_aluno == 'sair':
        break
    else:
        count_alunos += 1
        gabarito_aluno = str(input())
        for u in range(len(gabarito_aluno)):
            gab_lista_aluno.append(gabarito_aluno[u])
        for j in range(5):
            if gab_lista[j] == gab_lista_aluno[j]:
                count_nota += 20
        aluno_notas[nome_aluno] = count_nota
        notas.append(count_nota)

media_nota = sum(notas)/count_alunos
aluno_max = ''
count_alunos_media = 0

for nome, nota in aluno_notas.items():
    if nota == max(notas):
        aluno_max = nome
    if nota > media_nota:
        count_alunos_media += 1

print(count_alunos_media)
print(aluno_max)

