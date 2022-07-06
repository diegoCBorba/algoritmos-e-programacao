while True:
    jogadores = []
    numeros_int = [] # Para transformar os numeros em inteiros posteriormente
    jogo = input().split()
    if jogo == ['sair']:
        print('fim')
        exit(0)
    jogadores.extend([jogo[0], jogo[1]])
    jogo.pop(0)
    jogo.pop(0)
    if len(jogo) % 2 != 0:
        print('erro')
        exit(0)
    else:
        for nums in jogo:
            numeros_int.append(int(nums))

        # count impar = jogador 1 / count par = jogador 2
        count = 0
        pontuacao_1 = 0
        pontuacao_2 = 0
        for nums in range(len(numeros_int)):
            if (nums + 1) % 2 != 0:
                count += 1
                # se as duas cartas têm o mesmo valor
                if numeros_int[nums] == numeros_int[nums + 1]:
                    if count % 2 != 0:
                        pontuacao_1 += (numeros_int[nums] + numeros_int[nums]) * 2
                    else:
                        pontuacao_2 += (numeros_int[nums] + numeros_int[nums]) * 2

                elif (numeros_int[nums] + 1 == numeros_int[nums + 1]) or (numeros_int[nums] == numeros_int[nums + 1] + 1):
                    if count % 2 != 0:
                        pontuacao_1 += (numeros_int[nums] + numeros_int[nums + 1]) * 3
                    else:
                        pontuacao_2 += (numeros_int[nums] + numeros_int[nums + 1]) * 3

                else:
                    if count % 2 != 0:
                        pontuacao_1 += (numeros_int[nums] + numeros_int[nums + 1])
                    else:
                        pontuacao_2 += (numeros_int[nums] + numeros_int[nums + 1])

        if pontuacao_1 > pontuacao_2:
            print(jogadores[0])
        elif pontuacao_1 < pontuacao_2:
            print(jogadores[1])
        else:
            print('empate')
