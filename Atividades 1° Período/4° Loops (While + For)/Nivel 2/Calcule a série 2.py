n = int(input())
numerador = 1
denominador = 4
calculo = 0
print_soma = ''
count = 0

for i in range(n):
    count += 1
    if count != n:
        if count % 2 == 0:
            print_soma += " 1 +"
        else:
            if count == 1:
                print_soma += "{}/{} +".format(numerador, denominador)
            else:
                print_soma += " {}/{} +".format(numerador, denominador)
    else:
        if count % 2 == 0:
            print_soma += ' 1'
        else:
            if n == 1:
                print_soma += "{}/{}".format (numerador, denominador)
            else:
                print_soma += " {}/{}".format (numerador, denominador)

    if count % 2 == 0:
        calculo += 1
    else:
        calculo += (numerador/denominador)
        numerador += 2
        denominador += 4

print('{:.2f}'.format(calculo))
print(print_soma)

