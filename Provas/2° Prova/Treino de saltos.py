nota_total_atleta = 0
count_notas = 0

while True:
    nota_total_atleta = 0
    count_notas = 0
    nome = str(input())
    if nome == 'sair':
        break
    while True:
        nota_salto = float(input())
        if nota_salto < 0:
            break
        nota_total_atleta += nota_salto
        count_notas += 1
    if count_notas == 0:
        print('{}: 0.0'.format(nome, count_notas))
    else:
        media = nota_total_atleta / count_notas
        print('{}: {:.1f}'.format(nome, media))