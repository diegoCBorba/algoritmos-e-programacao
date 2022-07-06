while True:
    n_inicial = int(input())
    if 1 <= n_inicial <= 9:
        break
    elif n_inicial < 1 or n_inicial > 9:
        print("Insira um número inicial entre 1 e 9")

while True:
    n_final = int(input())
    if 1 <= n_final <= 9:
        break
    elif n_final < 1 or n_final > 0:
        print("Insira um número final entre 1 e 9")

if n_inicial > n_final:
    print("Nenhuma tabuada nesse intervalo")
    exit(0)

for x in range(n_inicial, n_final + 1):
    for i in range(1, 9 + 1):
        indice = x * i

        print("{} x {} = {}".format(x, i, indice))

        if i == 9:
            print("")

"""
if n_inicial == n_final:
    tab1 = n_inicial
    tab2 = n_inicial * 2
    tab3 = n_inicial * 3
    tab4 = n_inicial * 4
    tab5 = n_inicial * 5
    tab6 = n_inicial * 6
    tab7 = n_inicial * 7
    tab8 = n_inicial * 8
    tab9 = n_inicial * 9
    print("{} x 1 = {}".format(n_inicial, tab1))
    print("{} x 2 = {}".format(n_inicial, tab2))
    print("{} x 3 = {}".format(n_inicial, tab3))
    print("{} x 4 = {}".format(n_inicial, tab4))
    print("{} x 5 = {}".format(n_inicial, tab5))
    print("{} x 6 = {}".format(n_inicial, tab6))
    print("{} x 7 = {}".format(n_inicial, tab7))
    print("{} x 8 = {}".format(n_inicial, tab8))
    print("{} x 9 = {}".format(n_inicial, tab9))
    print('')
    exit(0)

for i in range(n_inicial, n_final + 1):
    tab1 = i
    tab2 = i * 2
    tab3 = i * 3
    tab4 = i * 4
    tab5 = i * 5
    tab6 = i * 6
    tab7 = i * 7
    tab8 = i * 8
    tab9 = i * 9
    print("{} x 1 = {}".format(i, tab1))
    print("{} x 2 = {}".format(i, tab2))
    print("{} x 3 = {}".format(i, tab3))
    print("{} x 4 = {}".format(i, tab4))
    print("{} x 5 = {}".format(i, tab5))
    print("{} x 6 = {}".format(i, tab6))
    print("{} x 7 = {}".format(i, tab7))
    print("{} x 8 = {}".format(i, tab8))
    print("{} x 9 = {}".format(i, tab9))
    print('')
"""
