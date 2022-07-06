n_array = int(input())
count = 0
lista1 = []
lista2 = []
lista_mista = []

for i in range(n_array):
    nums = int(input())
    lista1.append(nums)

for i in range(n_array):
    nums = int(input())
    lista2.append(nums)

for i in range(n_array):
    lista_mista.extend([lista1[i], lista2[i]])

