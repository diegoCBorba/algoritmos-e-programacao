"""
quant, num_soma = input().split()
quant = int(quant)
num_soma = int(num_soma)
lista = []
count = 0

n = map(int, input().split())

for i in n:
    i = int(i)
    lista.append(i)

for j in lista:
    for k in lista:
        if j == k:
            break
        if j + k == num_soma:
            count += 1
if count > 0:
    print("SIM")
    exit(0)
else:
    print("NAO")
"""

n, e = map(int, input().split())
condicao_presente = False
ideias = input().split()
valor_ideias = []

for i in ideias:
    valor_ideias.append(int(i))

for j in range(len(ideias)):
    for x in range(len(ideias)):
            if (valor_ideias[j] + valor_ideias[x] == e) and (j != x):
                condicao_presente = True
                break

if not condicao_presente:
    print('NAO')
else:
    print('SIM')
