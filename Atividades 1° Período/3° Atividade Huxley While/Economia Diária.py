"""
dias_semana = 0
meta_feita = 0
soma_dinheiro = 0

while dias_semana <= 6:

    if dias_semana == 0:
        valor1 = float(input())
        dias_semana += 1
        if dias_semana == 1:
            valor2 = float(input())
            diferenca = valor2 - valor1
            dias_semana += 1
            if diferenca >= 0.50:
                meta_feita += 1
            if dias_semana == 2:
                valor3 = float(input())
                diferenca = valor3 - valor2
                dias_semana += 1
                if diferenca >= 0.50:
                    meta_feita += 1
                if dias_semana == 3:
                    valor4 = float(input())
                    diferenca = valor4 - valor3
                    dias_semana += 1
                    if diferenca >= 0.50:
                        meta_feita += 1
                    if dias_semana == 4:
                        valor5 = float(input())
                        diferenca = valor5 - valor4
                        dias_semana += 1
                        if diferenca >= 0.50:
                            meta_feita += 1
                        if dias_semana == 5:
                            valor6 = float(input())
                            diferenca = valor6 - valor5
                            dias_semana += 1
                            if diferenca >= 0.50:
                                meta_feita += 1
                            if dias_semana == 6:
                                valor7 = float(input())
                                diferenca = valor7 - valor6
                                dias_semana += 1
                                if diferenca >= 0.50:
                                    meta_feita += 1

print("R$ {:.2f}".format(valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7))
print(meta_feita)

"""

dias = 7

valor_atual = 0
valor_anterior = 0
soma_dia = 0
meta_dia = 0

for i in range(dias):
    valor_anterior = valor_atual
    valor_atual = float(input())
    soma_dia = soma_dia + valor_atual
    diferenca = valor_atual - valor_anterior

    if diferenca >= 0.50 and i != 0:
        meta_dia += 1

print("R$ {:.2f}".format(soma_dia))
print(meta_dia)