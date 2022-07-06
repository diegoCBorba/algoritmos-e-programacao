l = ['C', 'O', 'B', 'O', 'L']

while True:
    count = 0
    codigo = input().upper().split("-")
    if codigo == ['FIM']:
        exit(0)
    for i in range(len(codigo)):
        for j in codigo[i]:
            if l[i] in j:
                count += 1
                break

    if count == 5:
        print("aquilo lá")
    else:
        print('bug')