n1 = int(input())
n2 = int(input())
lista_num = [n1, n2]


def verifica_primo(num):
    count = 0
    for nums in range(1, num[0] + 1):
        if num[0] % nums == 0:
            count += 1

    if count != 2:
        return 'O numero {} nao eh primo.'.format(num[0])

    count = 0
    for nums in range(1, num[1] + 1):
        if num[1] % nums == 0:
            count += 1

    if count != 2:
        return 'O numero {} nao eh primo.'.format(num[1])

    count = 0
    for nums in range(1, (num[0] + num[1]) + 1):
        if (num[0] + num[1]) % nums == 0:
            count += 1

    if count != 2:
        return 'A soma de {} e {} nao eh um primo.'.format(num[0], num[1])
    else:
        return 'A soma de {} e {} eh um primo.'.format(num[0], num[1])


print(verifica_primo(lista_num))

