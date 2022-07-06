salario_total_m = 0  # masculino
salario_total_f = 0  # feminino
maior_salario = 0
sexo_maior_salario = ''
count_m = 0
count_f = 0

for i in range(10):
    salario = float(input())
    sexo = str(input())
    if sexo == 'f':
        count_f += 1
        salario_total_f += salario
    else:
        count_m += 1
        salario_total_m += salario

    if salario > maior_salario:
        maior_salario = salario
        sexo_maior_salario = sexo

print(count_m)
print(count_f)
print("{:.1f}".format((salario_total_m + salario_total_f) / 10))
print(sexo_maior_salario)
print("{:.1f}".format(salario_total_m / count_m))
