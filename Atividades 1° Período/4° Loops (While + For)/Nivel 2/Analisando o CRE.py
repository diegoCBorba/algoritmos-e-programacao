"""
mat_aluno_menor_cre = 0
menor_cre = 11
soma_cre = 0
qtde_cre = 0

while True:
    mat = int(input())
    if mat == 999:
        break
    cre = float(input())
    soma_cre += cre
    qtde_cre += 1
    if cre < menor_cre:
        menor_cre = cre
        mat_aluno_menor_cre = mat

print(mat_aluno_menor_cre)
print("{:.2f}".format(soma_cre/qtde_cre))

"""
CRE_anteiror = 11
count = 0
total_cre = 0
matricula_menor = 0

while True:
    matricula_int = int(input())
    if matricula_int == 999:
        break
    count += 1
    CRE = float(input())
    total_cre += CRE

    if CRE < CRE_anteiror:
        matricula_menor = matricula_int
        CRE_anteiror = CRE

print("{}".format(matricula_menor))
print("{:.2f}".format(total_cre / count))
