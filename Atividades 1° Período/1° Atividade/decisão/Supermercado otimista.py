dia_da_semana = str(input())
preco_produto = float(input())
opcao_produto = str(input())
nome_produto = str(input())
valor = preco_produto * 2

if dia_da_semana == 'seg' or dia_da_semana == 'ter' or dia_da_semana == 'qua':
    if opcao_produto == 'ouro':
        valor = preco_produto * (1 / 2)

elif dia_da_semana == 'qui' or dia_da_semana == 'sex':
    if 10 <= preco_produto <= 100:
        valor = preco_produto / 3

elif dia_da_semana == 'sab':
    if opcao_produto == 'prata':
        valor = preco_produto * 3

print("O preco do produto {} no dia {} eh {:.2f}".format(nome_produto, dia_da_semana, valor))