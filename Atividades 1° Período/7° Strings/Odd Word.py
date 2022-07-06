frase = list(map(str, input().split()))
contador = 0

for palavras in range(len(frase)):
    contador += 1
    lista_letra = []
    if contador % 2 == 0:
        for letras in frase[palavras]:
            lista_letra.append(letras)
        lista_letra.reverse()
        frase[palavras] = ''.join(lista_letra)

print(' '.join(frase))
