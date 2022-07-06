salario = float(input())
horaextra= float (input())

SalarioF= ((salario/44)*1.1)*horaextra + salario

print("{:.2f}".format(SalarioF))