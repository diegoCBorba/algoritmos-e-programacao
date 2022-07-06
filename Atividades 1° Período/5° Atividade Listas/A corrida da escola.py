n_competidores, voltas_corrida = map(int, input().split())
tempo_comp = []

for i in range(n_competidores):
    voltas_comp = input().split()
    soma_tempo = 0
    for tempo_str in voltas_comp:
        soma_tempo += int(tempo_str)

    tempo_comp.append(soma_tempo)

x = min(tempo_comp)
print(tempo_comp.index(x) + 1)
