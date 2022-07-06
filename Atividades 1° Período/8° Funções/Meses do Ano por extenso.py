n = int(input())


def mes_do_ano(mes):
    if mes < 1 or mes > 12:
        return 'invalido'
    l_ano = {1: 'janeiro', 2: 'fevereiro', 3: 'marco', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho',
             8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    for num, meses in l_ano.items():
        if num == mes:
            return meses


print(mes_do_ano(n))