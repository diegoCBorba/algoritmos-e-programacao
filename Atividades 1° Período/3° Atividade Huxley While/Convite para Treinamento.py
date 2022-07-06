n_convidados = int(input())
nota_minima = int(input())
count = 0

for i in range(n_convidados):
    nota_x = int(input())
    nota_y = int(input())
    if (nota_x + nota_y) >= nota_minima and nota_x != 0 and nota_y != 0:
        count += 1

print(count)
