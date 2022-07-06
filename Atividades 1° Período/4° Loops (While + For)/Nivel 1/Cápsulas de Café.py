total_capsulas = 0

for i in range(7):
    qnt_pacotes = int(input())
    tipo_pacote = str(input())

    if tipo_pacote == 'P' or tipo_pacote == 'p':
        total_capsulas += (qnt_pacotes * 10)
    if tipo_pacote == 'G' or tipo_pacote == 'g':
        total_capsulas += (qnt_pacotes * 16)

print(total_capsulas)
print((total_capsulas * 2) // 7)