ini, fim = map(int, input().split())

ano_bissexto = False
for i in range(ini, fim + 1):
    if i % 100 == 0:
        if i % 400 == 0:
            ano_bissexto = True
            print(i)
    elif i % 4 == 0:
        ano_bissexto = True
        print(i)

if not ano_bissexto:
    print(-1)
