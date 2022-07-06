def eh_par(num):
    return num % 2 == 0


def ContaDigitosPares(num):
    if num == "":
        return 0
    if eh_par(int(num[0])):
        num = num[1:]
        return 1 + ContaDigitosPares(num)
    num = num[1:]
    return ContaDigitosPares(num)


n = input()
print(ContaDigitosPares(n))
