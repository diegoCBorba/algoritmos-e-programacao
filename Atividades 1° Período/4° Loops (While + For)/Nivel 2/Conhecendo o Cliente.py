quantidade_vendas = 0
total_vista = 0
total_cartao = 0
idade_mais_jovem = 150
valor_maior_compra = 0
count_vista = 0

while True:
    idade = int(input())
    valor_da_compra = float(input())
    tipo_pagamento = str(input())
    s_n = str(input())
    quantidade_vendas += 1

    if tipo_pagamento == 'V':
        total_vista += valor_da_compra
        count_vista += 1
    else:
        total_cartao += valor_da_compra

    if idade < idade_mais_jovem:
        idade_mais_jovem = idade

    if valor_da_compra > valor_maior_compra:
        valor_maior_compra = valor_da_compra

    if s_n == 'N':
        break

print(quantidade_vendas)
if total_vista == 0.00:
    print(0)
else:
    print("{:.2f}".format(total_vista))
if total_cartao == 0.00:
    print(0)
else:
    print("{:.2f}".format(total_cartao))
print(idade_mais_jovem)
print(valor_maior_compra)
if count_vista == 0:
    print(0)
else:
    print("{:.2f}".format(total_vista / count_vista))