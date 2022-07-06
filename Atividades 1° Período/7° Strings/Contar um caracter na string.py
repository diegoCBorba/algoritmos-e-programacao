palavra = input()
letra_escolhida = input()
count = 0
l = []

for i in palavra:
    l.append(i)

for letras in l:
    if letras == letra_escolhida:
        count += 1

print(count)