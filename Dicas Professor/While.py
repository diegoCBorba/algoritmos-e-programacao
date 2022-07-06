soma_notas = 0
notas_recebidas = 0

while True: # Laço que pega várias notas
    nota = 0
    while True: # Laço de validação dos dados
        nota = input() #vai sair string
        if nota == "Fim":
            break
        nota = int(nota)
        if 0 <= nota <= 10:
            break
        else:
            print("Nota fora do intervalo")

    if nota == "Fim":
        break
    soma_notas = soma_notas + nota
    notas_recebidas += 1