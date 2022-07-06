time_jogador = str(input())

if time_jogador == 'GSW':
    nome_jogador = str(input())
    arremesso_tentado2p = int(input())
    arremesso_convertido2p = int(input())
    arremesso_tentado3p = int(input())
    arremesso_convertido3p = int(input())

    pontos_totais = arremesso_convertido2p + arremesso_convertido3p
    percentual_2p = arremesso_convertido2p/arremesso_tentado2p
    percentual_3p = arremesso_convertido3p/arremesso_tentado3p

    if pontos_totais > 30 or percentual_2p > 0.5 or percentual_3p > 0.4:
        print("O time {} estah jogando, e {} estah indo bem.".format(time_jogador, nome_jogador))

    else:
        print("O time {} estah jogando, mas {} nao estah indo bem.".format(time_jogador, nome_jogador))

elif time_jogador == 'HOU':
    nome_jogador = str(input())
    arremesso_tentado2p = int(input())
    arremesso_convertido2p = int(input())
    arremesso_tentado3p = int(input())
    arremesso_convertido3p = int(input())

    pontos_totais = arremesso_convertido2p + arremesso_convertido3p
    percentual_2p = arremesso_convertido2p/arremesso_tentado2p
    percentual_3p = arremesso_convertido3p/arremesso_tentado3p

    if pontos_totais > 30 or percentual_2p > 0.5 or percentual_3p > 0.4:
        print("O time {} estah jogando, e {} estah indo bem.".format(time_jogador, nome_jogador))

    else:
        print("O time {} estah jogando, mas {} nao estah indo bem.".format(time_jogador, nome_jogador))

elif time_jogador == 'CLE':
    nome_jogador = str(input())
    arremesso_tentado2p = int(input())
    arremesso_convertido2p = int(input())
    arremesso_tentado3p = int(input())
    arremesso_convertido3p = int(input())

    pontos_totais = arremesso_convertido2p + arremesso_convertido3p
    percentual_2p = arremesso_convertido2p/arremesso_tentado2p
    percentual_3p = arremesso_convertido3p/arremesso_tentado3p

    if pontos_totais > 30 or percentual_2p > 0.5 or percentual_3p > 0.4:
        print("O time {} estah jogando, e {} estah indo bem.".format(time_jogador, nome_jogador))

    else:
        print("O time {} estah jogando, mas {} nao estah indo bem.".format(time_jogador, nome_jogador))

elif time_jogador == 'BOS':
    nome_jogador = str(input())
    arremesso_tentado2p = int(input())
    arremesso_convertido2p = int(input())
    arremesso_tentado3p = int(input())
    arremesso_convertido3p = int(input())

    pontos_totais = arremesso_convertido2p + arremesso_convertido3p
    percentual_2p = arremesso_convertido2p/arremesso_tentado2p
    percentual_3p = arremesso_convertido3p/arremesso_tentado3p

    if pontos_totais > 30 or percentual_2p > 0.5 or percentual_3p > 0.4:
        print("O time {} estah jogando, e {} estah indo bem.".format(time_jogador, nome_jogador))

    else:
        print("O time {} estah jogando, mas {} nao estah indo bem.".format(time_jogador, nome_jogador))

else:
    print("Nenhum time de interesse jogando.")