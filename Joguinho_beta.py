while True:

    print("Bem-vindo ao joguinho\n")
    print("Soldado, você precisa chegar no campo inimigo e para isso\nestou te dando um mapa da localização exata",end=' ')
    print("das bombas do inimigo.")
    print("Sua tarefa é decorar a posição das bombas 'o' e fazer seu personagem 'x'\nchegar até o final sem pisar nelas\n")

    lista_matriz = []
    count = 0

    import random

    def posicao_inicial():
        """
        Função que exerce o papel de dar um índice possível inicial para ser utilizado
        posteriormente para a posição inicial de 'x'.
        :return: O valor entre 0 e 7
        """
        valor = random.randint(0, 7)
        return valor


    def zero_ou_um():
        """
        Função que exerce o papel de crial um valor randômico entre 0 e 1 para ser utilizado posteriormente
        na linha das matrizes criadas.
        :return:
        """
        valor = random.random()
        if valor > 0.5:
            return 0
        return 1


    # Armazena a posição de x para ser trocada na linha inicial da matriz
    pos_x = posicao_inicial()

    # Esse 'for' em sua totalidade serve para criar a matriz que representa o mapa do jogo e colocar o personagem no mapa
    # de forma aleatória.

    for j in range(8):
        linhas = []
        count += 1
        for x in range(8):
            if count % 2 != 0:
                linhas.append(zero_ou_um())
            else:
                linhas.append(0)
                # Esse if serve para trocar algum zero da posição da linha inicial pelo personagem
                if j == 7 and x == 7:
                    linhas.insert(pos_x, 'x')
                    linhas.pop(pos_x + 1)

        while True:
            if linhas == [1, 1, 1, 1, 1, 1, 1, 1]:
                linhas = []
                for j in range(8):
                    linhas.append(zero_ou_um())
            else:
                lista_matriz.append(linhas)
                break

    contador_linha = 0
    for linha in lista_matriz:
        contador = 0
        contador_linha += 1
        for coluna in linha:
            contador += 1
            if coluna == 0:
                print('\033[1;32m_', end=' ')
            elif coluna == 1:
                print('\033[1;31mo', end=' ')
            else:
                print('\033[1;33mx', end=' ')
            if contador == 8:
                print(f'\033[0;0mlinha {contador_linha}', end='')
        print()


    def posicao_do_x():
        """
        Essa função exerce o papel de realizar um 'for' para achar em qual lista dentro da lista principal está o x e
        posteriormente armazenar o o indice dentro dessa lista em que o personagem está, sempre
        informando sua posição exata.
        :return: Uma lista informando no índice 0 a linha de x e o índice 1 informando a coluna
        """
        for i in lista_matriz:
            for j in i:
                if j == 'x':
                    linha_de_x = lista_matriz.index(i)
                    coluna_de_x = i.index(j)
                    break
        return [linha_de_x, coluna_de_x]


    # Aqui neste While está basicamente o jogo que realiza a movimentação do 'x', no caso o personagem e diz se ele
    # venceu ou não.
    sair = False
    while True:
        while True:
            linha = int(input("\033[0;0mDigite qual linha você quer seguir: "))
            if 1 <= linha <= 8:
                if -1 <= (linha - 1) - posicao_do_x()[0] <= 1:
                    break
                else:
                    print("Digite uma linha adjacente ao personagem.")
            else:
                print("Digite um número dentro do intervalo (1 a 8)")

        while True:
            coluna = int(input("Digite qual coluna você quer seguir: "))
            if 1 <= coluna <= 8:
                if (linha - 1) == posicao_do_x()[0]:
                    if -1 <= (coluna - 1) - posicao_do_x()[1] <= 1:
                        break
                    else:
                        print("Digite uma linha adjacente ao personagem.")
                else:
                    if (coluna - 1) - posicao_do_x()[1] == 0:
                        break
                    else:
                        print("Digite uma coluna adjacente ao personagem.")

            else:
                print("Digite um número dentro do intervalo (1 a 8)")

        if lista_matriz[linha - 1][coluna - 1] == 1:
            print("Você perdeu o jogo")
            break

        # tira o x de sua posição inicial e acrescenta o zero
        for i in lista_matriz[posicao_do_x()[0]]:
            if i == 'x':
                lista_matriz[posicao_do_x()[0]].insert(posicao_do_x()[1], 0)
                lista_matriz[posicao_do_x()[0]].remove('x')

        # Tira o 0 de sua posição e acrescenta o x
        lista_matriz[linha - 1].insert(coluna - 1, 'x')
        lista_matriz[linha - 1].pop(coluna)

        contador_linha = 0
        for linha in lista_matriz:
            contador = 0
            contador_linha += 1
            for coluna in linha:
                contador += 1
                if coluna != 'x':
                    print('\033[1;32m_', end=' ')
                else:
                    print('\033[1;33mx', end=' ')
                if contador == 8:
                    print(f'\033[0;0m| L{contador_linha}')

        for i in lista_matriz[0]:
            if i == 'x':
                print("Você conseguiu chegar no final, parabéns!!!")
                sair = True

        if sair:
            break

    print("Você deseja jogar novamente?")
    saida = input(str("'Sim' ou 'Não': "))
    if saida == 'Sim':
        sair = False
        lista_matriz.clear()
    else:
        print('Até outra hora!')
        exit(0)