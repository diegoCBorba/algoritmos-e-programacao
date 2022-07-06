ano_atual = 0
ano_mnovo = 0
soma_dia = 0
velocidade_atual = 0
velocidade_maior = 0
velocidadetotal = 0
count = 0
q_situacao = str(input())

if q_situacao == "N" or q_situacao == "n":
    print("zero")
    exit(0)

while True:
    ano_atual = int(input())
    velocidade_atual = float(input())
    q_situacao = str(input())
    velocidadetotal += velocidade_atual
    count += 1
    if ano_atual >= ano_mnovo:
        ano_mnovo = ano_atual
    if velocidade_atual >= velocidade_maior:
        velocidade_maior = velocidade_atual
    if q_situacao == "N" or q_situacao == "n":
        break

print("{:.2f}".format(velocidade_maior))
print("{:.0f}".format(ano_mnovo))
print("{:.2f}".format(velocidadetotal / count))
