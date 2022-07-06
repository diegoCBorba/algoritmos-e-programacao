lista_op_valor = []
soma_credito = 0
soma_debito = 0

while True:
    opc_e_valor = list(map(float, input().split()))
    if opc_e_valor == [-1]:
        break
    lista_op_valor.append(opc_e_valor)

for linha in range(len(lista_op_valor)):
    if lista_op_valor[linha][0] == 1.0:
        soma_credito += lista_op_valor[linha][1]
    else:
        soma_debito += lista_op_valor[linha][1]

print('Creditos: R$ {:.2f}'.format(soma_credito))
print('Debitos: R$ {:.2f}'.format(soma_debito))
print('Saldo: R$ {:.2f}'.format(soma_credito-soma_debito))

