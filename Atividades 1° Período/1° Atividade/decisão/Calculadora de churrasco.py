opcao_carne = str(input())

CB = 32
CF = 18
CS = 15
GC = 8
GR = 6

if opcao_carne == 'C':
    pao_de_alho = str(input())
    bebida_adulto = str(input())
    bebida_crianca = str(input())
    qnt_crianca = int(input())
    qnt_adulto = int(input())
    if pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = chuC + bebidas
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = chuC + bebidas
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = chuC
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = chuC * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = (chuC + bebidas) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = (chuC + bebidas) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                    (CB * 0.2) * qnt_crianca)
        total = chuC + bebidas
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuC = ((CB * 0.2) * qnt_adulto) + ((CF * 0.1) * qnt_adulto) + ((CS * 0.1) * qnt_adulto) + (
                (CB * 0.2) * qnt_crianca)
        total = (chuC + bebidas)
        print("R$: {:.2f}".format(total))

elif opcao_carne == 'BF':
    pao_de_alho = str(input())
    bebida_adulto = str(input())
    bebida_crianca = str(input())
    qnt_crianca = int(input())
    qnt_adulto = int(input())
    if pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = bebidas + chuBF
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = bebidas + chuBF
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = chuBF
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = chuBF * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBF) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBF) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBF) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuBF = ((CB * 0.25) * qnt_adulto) + ((CF * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = bebidas + chuBF
        print("R$: {:.2f}".format(total))

elif opcao_carne == 'BS':
    pao_de_alho = str(input())
    bebida_adulto = str(input())
    bebida_crianca = str(input())
    qnt_crianca = int(input())
    qnt_adulto = int(input())
    if pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = bebidas + chuBS
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = bebidas + chuBS
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = chuBS
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'N':
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = chuBS * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'S':
        bebidas = ((2 * GC) * qnt_adulto) + ((0.5 * GR) * qnt_crianca)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBS) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBS) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'N' and bebida_adulto == 'S' and bebida_crianca == 'N':
        bebidas = ((2 * GC) * qnt_adulto)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBS) * 0.98
        print("R$: {:.2f}".format(total))

    elif pao_de_alho == 'S' and bebida_adulto == 'N' and bebida_crianca == 'S':
        bebidas = ((0.5 * GR) * qnt_crianca)
        chuBS = ((CB * 0.25) * qnt_adulto) + ((CS * 0.15) * qnt_adulto) + ((CB * 0.2) * qnt_crianca)
        total = (bebidas + chuBS) * 0.98
        print("R$: {:.2f}".format(total))

else:
    print("Opção inválida.")