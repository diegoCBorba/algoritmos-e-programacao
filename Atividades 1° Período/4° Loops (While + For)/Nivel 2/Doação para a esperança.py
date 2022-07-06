soma_atual = 0
soma_para_o_mes = 0

while True:
    valor = int(input())

    if valor < 1:
        break

    tipo_doacao = int(input())

    if not (tipo_doacao == 1 or tipo_doacao == 2):
        while tipo_doacao == 1 or tipo_doacao == 2:
            print("Valor invalido")
            tipo_doacao = int(input())
            if tipo_doacao == 1 or tipo_doacao == 2:
                break

    if tipo_doacao == 2:
        quantidade_meses = int(input())
        if not 2 <= quantidade_meses <= 12:
            while True:
                print("Favor digitar valor entre 2 e 12, inclusive")
                quantidade_meses = int(input())
                if 2 <= quantidade_meses <= 12:
                    break
        soma_para_o_mes += (valor * (quantidade_meses - 1))
        soma_atual += valor

    else:
        soma_atual += valor

print("Total arrecadado para agora: R$ {:.2f}".format(soma_atual))
print("Total arrecadado para meses futuros: R$ {:.2f}".format(soma_para_o_mes))
