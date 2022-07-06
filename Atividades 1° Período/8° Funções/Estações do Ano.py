"""
Primavera: 21 setembro(9) até 20 dezembro(12)
Verão: 21 dezembro(12) até 20 março(3)
Outono: 21 março(3) até 20 junho(6)
Inverno: 21 junho(6) até 20 setembro(9)
"""
dia = int(input())
mes = int(input())


def EstacaoAno(dia, mes):
    if (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        return 'PRIMAVERA'
    elif (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        return 'VERAO'
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        return 'OUTONO'
    return 'INVERNO'


print(EstacaoAno(dia, mes))