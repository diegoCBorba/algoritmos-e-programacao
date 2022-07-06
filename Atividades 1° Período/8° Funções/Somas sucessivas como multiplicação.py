n = int(input())
mult = int(input())


def multiplicacao_sucessiva(numero, multi):
    soma = 0
    if multi < 0 and numero > 0:
        numero = numero * -1
        multi = multi * -1
    elif multi < 0 and numero < 0:
        multi = multi * -1
    for i in range(multi):
        soma += numero
    return soma


print(multiplicacao_sucessiva(n, mult))
