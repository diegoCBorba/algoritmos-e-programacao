"""
n = int(input())


def eh_par(num):
    return num % 2 == 0


def contaPares(num):
    if num < 0:
        return ''
    if eh_par(num):
        print(num)
    return contaPares(num - 1)


contaPares(n)
"""

n = int(input())
count = 0


def eh_par(n):
    return n % 2 == 0


def contaPares(n, count):
    if count > n:
        return ''
    if eh_par(count):
        print(count)
    return contaPares(n, count + 1)


contaPares(n, count)