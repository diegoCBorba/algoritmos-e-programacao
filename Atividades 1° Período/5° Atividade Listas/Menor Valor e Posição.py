n = int(input())
nums_str = input().split()
nums_int = []

for i in range(n):
    nums_int.append(int(nums_str[i]))

indereco_min = min(nums_int)

print('Menor valor: {}'.format(indereco_min))
print('Posicao: {}'.format(nums_int.index(indereco_min)))
