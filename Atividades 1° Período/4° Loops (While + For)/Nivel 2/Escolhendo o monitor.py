media_anterior = 0
count = 0
nome_nota_maior = ''

while True:
    media_disciplina = int(input())
    if not 0 <= media_disciplina <= 100:
        while True:
            print('Nota fora do intervalo')
            media_disciplina = int(input())
            if 0 <= media_disciplina <= 100:
                break
    if media_disciplina == 0:
        break

    nome_candidato = str(input())
    tempo_disponivel = int(input())
    if media_disciplina < 70 or tempo_disponivel < 8:
        print('Aluno NAO pode concorrer.')
    else:
        CRE = int(input())
        nota_prova_monitoria = int(input())
        if not 0 <= nota_prova_monitoria <= 100:
            while True:
                print('Nota fora do intervalo')
                nota_prova_monitoria = int(input())
                if 0 <= nota_prova_monitoria <= 100:
                    break
        media_final = ((media_disciplina * 4) + CRE + (nota_prova_monitoria * 5)) / 10

        if nota_prova_monitoria < 70:
            print('Aluno reprovado na prova de monitoria!')

        elif media_final < 70:
            print('Aluno reprovado na selecao. Media= {:.2f}.'.format(media_final))

        elif media_final >= 70:
            print('Aluno aprovado! Sua media foi {:.2f}.'.format(media_final))
            count += 1
            if media_final > media_anterior:
                media_anterior = media_final
                nome_nota_maior = nome_candidato

if count == 0:
    print('Resultado da monitoria: Sem alunos aprovados.')

else:
    print('Resultado da monitoria: {}, {:.2f}.'.format(nome_nota_maior, media_anterior))
