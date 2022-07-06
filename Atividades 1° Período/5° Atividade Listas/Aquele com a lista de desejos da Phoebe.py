num_desejo = int(input())
lista_desejo = []
lista_realizado = []
lista_index = []

for i in range(num_desejo):
    desejo = str(input())
    lista_desejo.append(desejo)

numero_desejo = len(lista_desejo)

num_realizado = int(input())

for j in range(num_realizado):
    realizado = str(input())
    lista_realizado.append(realizado)

for x in lista_realizado:
    for j in lista_desejo:
        if x == j:
            numero_desejo -= 1
            lista_index.append(lista_desejo.index(x))

if numero_desejo == 0:
    print('Smelly Cat, Smelly Cat, what are they feeding you?')

else:
    print(f"Ainda falta(m) {numero_desejo} objetivo(s)!")
    for u in lista_index:
        del lista_desejo[u]
    for q in lista_desejo:
        print(q)


