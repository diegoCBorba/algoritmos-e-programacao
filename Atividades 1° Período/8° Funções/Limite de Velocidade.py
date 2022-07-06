vel = int(input())


def CalculaMulta(velocidade):
    if velocidade <= 50:
        return '0.00'
    elif 50 < velocidade <= 55:
        return '230.00'
    elif 55 < velocidade <= 60:
        return '340.00'
    return '{:.2f}'.format((velocidade - 50) * 19.28)


print(CalculaMulta(vel))
