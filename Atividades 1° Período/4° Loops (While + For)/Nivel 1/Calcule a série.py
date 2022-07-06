numero = int(input())
calculo_total = 0

if numero == 0:
    print("0.00")
    exit(0)

calculo_print_total = ''
ultimo_numero = (numero / (numero * 3))
ultimo_numero_print = "{}/{}".format(numero, numero * 3)

for i in range(1, numero):
    numerador = i
    denominador = i * 3
    calculo = numerador / denominador
    calculo_total += calculo
    calculo_print = "{}/{} + ".format(numerador, denominador)
    calculo_print_total += calculo_print

print(calculo_print_total + ultimo_numero_print)
print("{:.2f}".format(calculo_total + ultimo_numero))

"""
if i == n -1:
    print("{}/{} +".format(dividendo, divisor, end=" "))
else:
    print("{}/{}".format(dividendo, divisor, end=""))
"""
