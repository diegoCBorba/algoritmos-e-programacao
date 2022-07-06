valor_anterior = 0
valor_pessoa = 0
valor_total = float(input())
numero_total = int(input())
soma_valor = 0
string_anterior = ''
nome = ''
if numero_total == 0:
    print("Nao ha conta ou funcionario suficiente para pagar a conta")
    exit(0)

for i in range(numero_total):
    valor_anterior = valor_pessoa
    string_anterior = nome
    nome = str(input())
    valor_pessoa = float(input())
    soma_valor += valor_pessoa
    if valor_anterior < valor_pessoa:
        nome_maior = nome
        valor_maior = valor_pessoa

print("{} pagou R$ {:.1f}".format(nome_maior, valor_maior))
if soma_valor >= valor_total:
    resto = soma_valor - valor_total
    print("Valor excedente: sobra R$  {:.1f}".format(resto))
else:
    falta = valor_total - soma_valor
    print("Valor insuficiente: falta R$  {:.1f}".format(falta))