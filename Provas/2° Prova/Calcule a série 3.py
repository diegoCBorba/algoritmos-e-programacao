n = int(input())
numerador = 1
denominador = 3
calculo = 0
print_soma = ''
count = 0
numerador_x = 1
numero_1 = 1

if n == 0:
    print('Sem termos para somar')
    exit(0)
if n == 1:
    print('1.00')
    print('1')
    exit(0)

for i in range(n):
    count += 1
    if count != n:
        if count % 2 != 0:
            if count == 1:
                print_soma += "{} +".format(numero_1)
            else:
                print_soma += " {} +".format(numero_1)
        else:
            if count != 1:
                print_soma += " {}/{} +".format(numerador_x, denominador)
            else:
                print_soma += " {}/{} +".format(numerador_x, denominador)
    else:
        if count % 2 != 0:
            print_soma += ' {}'.format(numero_1)
        else:
            if n == 1:
                print_soma += "{}/{}".format (numerador_x, denominador)
            else:
                print_soma += " {}/{}".format (numerador_x, denominador)

    if count % 2 != 0:
        calculo += numero_1
        numero_1 += 1
    else:
        calculo += (numerador_x/denominador)
        numerador += 1
        numerador_x = numerador**2
        denominador += 3

print('{:.2f}'.format(calculo))
print(print_soma)

