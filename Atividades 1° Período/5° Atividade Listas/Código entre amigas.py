lista = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
frase_final = []

while True:
    frase = input().split()
    if frase == ['6', '9', '13']:
        break
    frase_int = []
    frase_int.clear()
    frase_final.clear()
    for i in frase:
        frase_int.append(int(i))
    for j in frase_int:
        frase_final.append(lista[j])
    print(''.join(frase_final))

