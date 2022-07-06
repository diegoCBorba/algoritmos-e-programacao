num_1lista = int(input())
if num_1lista == 0:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
    exit(0)
lista_total = []
for i in range(num_1lista):
    num = int(input())
    lista_total.append(num)

num_2lista = int(input())
if num_2lista == 0:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
    exit(0)
for p in range(num_2lista):
    num = int(input())
    lista_total.append(num)

for k in range(len(lista_total)):
    if k == len(lista_total) - 1:
        print(lista_total[k])
    else:
        print(lista_total[k], end=' ')
