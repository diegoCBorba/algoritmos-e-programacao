seq_genetica = input()
base = input()
seq_lista = []
seq_indices_repitadas = []
contadores = []
primeiro_indice = []

for bases in seq_genetica:
    seq_lista.append(bases)

if base not in seq_lista:
    print('ERRO')

else:
    for indice in range(len(seq_lista)):
        if seq_lista[indice] == base:
            seq_indices_repitadas.append(indice)

    count = 1
    for indices in range(len(seq_indices_repitadas)):
        if indices != 0:
            if seq_indices_repitadas[indices] == (seq_indices_repitadas[indices - 1] + 1):
                if count == 1:
                    primeiro_indice.append(seq_indices_repitadas[indices - 1])
                count += 1
            else:
                contadores.append(count)
                if indices != len(seq_indices_repitadas):
                    count = 1

        if indices == (len(seq_indices_repitadas) - 1):
            primeiro_indice.append(seq_indices_repitadas[indices])
            contadores.append(count)

    maximo = max(contadores)
    ind_max = contadores.index(maximo)
    print(primeiro_indice[ind_max])
    print(max(contadores))


