n = int(input())
x_str = input().split()
x_num_int = []
count_num = 0
numeros_iguais = {}

for i in x_str:
    x_num_int.append(int(i))

x_num_int_sort = x_num_int.copy()
x_num_int_sort.sort()

for i in range(len(x_num_int)):
    if x_num_int[i] == x_num_int_sort[i]:
        numeros_iguais[x_num_int[i]] = i + 1
        count_num += 1

print(count_num)
for valor, indice in numeros_iguais.items():
    print(f'{valor} {indice}')

