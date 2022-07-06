jogador_menor_pontos = ''
jogador_maior_pontos = ''
menor_pontos = 1000
maior_pontos = 0
count = 0
numeros_jogadores = 0
total_pontos = 0

while True:
    nome_jogador = str(input())
    if nome_jogador == 'sair' and count == 0:
        print('Nenhum jogador foi registrado.')
        exit(0)
    elif nome_jogador == 'sair' and count > 0:
        break
    else:
        count += 1
        numeros_jogadores += 1
        qtde_pontos = int(input())

        if qtde_pontos <= menor_pontos:
            menor_pontos = qtde_pontos
            jogador_menor_pontos = nome_jogador

        if qtde_pontos >= maior_pontos:
            maior_pontos = qtde_pontos
            jogador_maior_pontos = nome_jogador

        total_pontos += qtde_pontos

print(jogador_menor_pontos)
print(jogador_maior_pontos)
print("{:.2f}".format(total_pontos/numeros_jogadores))