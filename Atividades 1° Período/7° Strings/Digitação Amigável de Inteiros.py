n_acetaveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'o', 'O', 'l']
while True:
    erro_ou_n = False
    n = input()
    if n == 'FIM':
        exit(0)
    l_numero = []
    l_int = []
    for num in n:
        l_numero.append(num)
    for numeros in l_numero:
        if numeros not in n_acetaveis:
            erro_ou_n = True
    if erro_ou_n:
        print('ERRO')
    else:
        for numeros in range(len(l_numero)):
            if l_numero[numeros] == 'o' or l_numero[numeros] == 'O':
                l_numero[numeros] = '0'
            elif l_numero[numeros] == 'l':
                l_numero[numeros] = '1'

        for numeros in l_numero:
            l_int.append(int(numeros))
        while True:
            if l_int[0] == 0:
                l_int.pop(0)
            else:
                break
        for numeros in range(len(l_int)):
            if numeros == (len(l_int) - 1):
                print(l_int[numeros])
            else:
                print(l_int[numeros], end='')
