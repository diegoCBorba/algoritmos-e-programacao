a, b, c = map(int, input().split())


def o_maior(a1, b2, c3):
    l = []
    l.extend([a1, b2, c3])
    return f'{max(l)} eh o maior'


print(o_maior(a, b, c))