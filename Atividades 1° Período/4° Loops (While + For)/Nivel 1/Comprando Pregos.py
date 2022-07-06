total_pregos = 0

while True:
    n_pregos = int(input())

    if n_pregos % 2 != 0:
        break

    total_pregos += n_pregos

if total_pregos % 12 != 0:
    numero_caixa = ((total_pregos - n_pregos) // 12) + 1
    print("{:.2f}".format(numero_caixa * 7.89))
    print((numero_caixa * 12)-total_pregos)

else:
    numero_caixa = (total_pregos - n_pregos) // 12
    print("{:.2f}".format(numero_caixa))
    print(0)
