tipo_ape = input().upper()
qnt_dias = int(input())


def CalculaHospedagem(tipo, dias):
    if tipo == 'INDIVIDUAL':
        if dias >= 3:
            return '{:.2f}'.format((125*dias)*0.85)
        else:
            return '{:.2f}'.format(125 * dias)

    elif tipo == 'SUÍTE DUPLA':
        if dias >= 3:
            return '{:.2f}'.format((140 * dias) * 0.85)
        else:
            return '{:.2f}'.format(140 * dias)

    else:
        if dias >= 3:
            return '{:.2f}'.format((180 * dias) * 0.85)
        else:
            return '{:.2f}'.format(180 * dias)


print(CalculaHospedagem(tipo_ape, qnt_dias))