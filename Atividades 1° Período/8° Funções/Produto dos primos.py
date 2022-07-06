"""
a, b, c, d = map(int, input().split())


def produto_primo(x, y, z, k):
    l = []
    l.extend([x, y, z, k])
    eh_primo = True
    for num in l:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count != 2:
            eh_primo = False

    if not eh_primo:
        return 'SEM PRODUTO'
    return x * y * z * k


print(produto_primo(a, b, c, d))
"""

a, b, c, d = map(int, input().split())


def produto_primo(x, y, z, k):
    l = []
    l.extend([x, y, z, k])
    for num in l:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count != 2:
            return 'SEM PRODUTO'
    return x * y * z * k


print(produto_primo(a, b, c, d))
