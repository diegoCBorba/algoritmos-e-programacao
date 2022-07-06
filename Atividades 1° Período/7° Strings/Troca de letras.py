palavras = []

while True:
    l_letras = []
    palavra = str(input()).upper()
    for letra in palavra:
        l_letras.append(letra)
    for letras in range(len(l_letras)):
        if l_letras[letras] == '3':
            l_letras[letras] = 'E'
        elif l_letras[letras] == '4':
            l_letras[letras] = 'A'
        elif l_letras[letras] == '1':
            l_letras[letras] = 'I'
        elif l_letras[letras] == '5':
            l_letras[letras] = 'S'
    if l_letras == ['S', 'A', 'I', 'R']:
        break
    palavras.append(''.join(l_letras))

for i in palavras:
    print(i)
