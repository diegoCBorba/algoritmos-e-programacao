codigo = input()
l_caracter = []

for caracter in codigo:
    l_caracter.append(caracter)

if l_caracter[6] == 'b':
    print('Bulbassauro')

elif l_caracter[6] == 'c':
    print('Charmander')

elif l_caracter[6] == 's':
    print('Squirtle')
else:
    print('Codigo Invalido')
