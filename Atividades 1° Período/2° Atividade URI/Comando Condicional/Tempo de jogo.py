a, b = map(float, input().split())

if a > b:
    duracao = (24 - a) + b

elif a < b:
    duracao = b - a

elif a == b:
    duracao = 24

print("O JOGO DUROU {:.0f} HORA(S)".format(duracao))
