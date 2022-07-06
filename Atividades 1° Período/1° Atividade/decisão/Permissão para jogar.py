idade_jogador = int(input())

if 0 <= idade_jogador <= 130:
    tipo_de_jogo = str(input())
    if tipo_de_jogo == 'azar':
        if idade_jogador >= 21:
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")

    elif tipo_de_jogo == 'mmorpg':
        if idade_jogador >= 14:
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")

    elif tipo_de_jogo == 'moba':
        if idade_jogador >= 10:
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")

    elif tipo_de_jogo == 'casual':
        print("Pode entrar!")

    else:
        print("Jogo invalido.")

else:
    if idade_jogador < 0 or idade_jogador > 130:
        print('Idade invalida.')
