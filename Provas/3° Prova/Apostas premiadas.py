gab_oficial = input().split()
ganhadores = 0
lista_contados = []

while True:
    gab_certos = 0
    apostas = input().split(",")
    lista_contados.clear()
    if apostas == ['FIM']:
        break
    for i in apostas:
        for j in gab_oficial:
            if i == j and i not in lista_contados:
                lista_contados.append(j)
                gab_certos += 1

    if gab_certos == 6:
        ganhadores += 1

    apostas.clear()

print(f"Total de ganhadores: {ganhadores}")
