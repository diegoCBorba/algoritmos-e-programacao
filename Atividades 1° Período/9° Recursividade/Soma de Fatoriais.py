def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num - 1)


def eh_divisor_3(num):
    return num % 3 == 0


def soma_fatoriais(num):
    if num == []:
        return 0
    if eh_divisor_3(num[0]):
        x = fatorial(num[0])
        num.pop(0)
        return x + soma_fatoriais(num)
    num.pop(0)
    return soma_fatoriais(num)


l = []
for i in range(5):
    n = int(input())
    l.append(n)

print(soma_fatoriais(l))