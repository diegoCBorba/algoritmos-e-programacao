media = float(input())
falta = int(input())


def ClassificaAluno(nota, faltas):
    if faltas > 10:
        return 'REPROVADO POR FALTAS'
    elif nota < 7:
        return 'REPROVADO'
    elif 7 <= nota < 9.5:
        return 'APROVADO'
    return 'APROVADO COM LOUVOR'


print(ClassificaAluno(media, falta))
