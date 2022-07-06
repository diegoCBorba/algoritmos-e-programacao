palavra = str(input())


def qnts_digitos(pal):
    l = []
    count = 0
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for digitos in palavra:
        l.append(digitos)
    for digitos in l:
        if digitos in nums:
            count += 1
    return count


print(qnts_digitos(palavra))