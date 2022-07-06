"""
for z in range(5):
    print("par[{}] = {}".format(z, lista_par[z]))

for x in range(5):
    print("impar[{}] = {}".format(x, lista_impar[x]))

for m in indice:
    del lista_par[m]
    del lista_impar[m]

for p in lista_impar:
    print("impar[{}] = {}".format(lista_impar.index(p), p))

for v in lista_par:
    print("par[{}] = {}".format(lista_par.index(v), v))
"""

"""
lista_total = []
lista_impar = []
lista_par = []
indice = [0, 0, 0, 0, 0]
for i in range(15):
    nums = int(input())
    lista_total.append(nums)
    if nums % 2 == 0:
        lista_par.append(nums)
    else:
        lista_impar.append(nums)

nums_restantes = len(lista_total)

while nums_restantes > 0:
    if len(lista_par) >= 5 or len(lista_impar) >= 5:
        if len(lista_par) >= 5:
            for a in range(5):
                print("par[{}] = {}".format(a, lista_par[a]))
            for m in indice:
                del lista_par[m]
            nums_restantes -= 5

        if len(lista_impar) >= 5:
            for b in range(5):
                print("impar[{}] = {}".format(b, lista_impar[b]))
            for m in indice:
                del lista_impar[m]
            nums_restantes -= 5
    else:
        if len(lista_impar) > 0:
            for d in range(len(lista_impar)):
                print("impar[{}] = {}".format(d, lista_impar[d]))
            nums_restantes -= len(lista_impar)
        if len(lista_par) > 0:
            for c in range(len(lista_par)):
                print("par[{}] = {}".format(c, lista_par[c]))
            nums_restantes -= len(lista_par)
            
"""

lista_total = []
lista_impar = []
lista_par = []
indice = [0, 0, 0, 0, 0]
for i in range(15):
    nums = int(input())
    lista_total.append(nums)
    if nums % 2 == 0:
        lista_par.append(nums)
        if len(lista_par) == 5:
            for a in range(5):
                print("par[{}] = {}".format(a, lista_par[a]))
            for m in indice:
                del lista_par[m]
    else:
        lista_impar.append(nums)
        if len(lista_impar) == 5:
            for b in range(5):
                print("impar[{}] = {}".format(b, lista_impar[b]))
            for m in indice:
                del lista_impar[m]

if len(lista_impar) > 0:
    for d in range(len(lista_impar)):
        print("impar[{}] = {}".format(d, lista_impar[d]))
if len(lista_par) > 0:
    for c in range(len(lista_par)):
        print("par[{}] = {}".format(c, lista_par[c]))

