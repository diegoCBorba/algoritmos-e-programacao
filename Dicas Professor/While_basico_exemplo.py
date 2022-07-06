qtde_notas = 0
soma_notas = 0

while qtde_notas < 3:
    nota = int(input())
    soma_notas = soma_notas + nota
    qtde_notas += 1

print("Média = {:.2f}".format(soma_notas/3))