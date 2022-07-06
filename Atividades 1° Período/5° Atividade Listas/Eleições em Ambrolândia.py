lista_votos = []
while True:
    votos = int(input())
    if votos == -1:
        break
    lista_votos.append(votos)

votos_candidato_83 = 0  # Alibabá
votos_candidato_93 = 0  # Alcapone
votos_branco = 0
votos_nulos = 0

for i in lista_votos:
    if i == 83:
        votos_candidato_83 += 1
    elif i == 93:
        votos_candidato_93 += 1
    elif i == 0:
        votos_branco += 1
    else:
        votos_nulos += 1

total = votos_branco + votos_candidato_83 + votos_candidato_93
print(votos_candidato_83)
print(votos_candidato_93)
print(votos_branco)
print(votos_nulos)
if votos_candidato_83 > votos_candidato_93:
    print(83)
else:
    print(93)
print("{:.2f}".format((votos_candidato_83/total)*100))
print("{:.2f}".format((votos_candidato_93/total)*100))
