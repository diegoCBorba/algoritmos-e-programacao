conjunto1 = int(input())
conjunto2 = int(input())
conj1 = []
conj2 = []
intersecao = []
diferenca = []
uniao = []
contados = []

for i in range(conjunto1):
    num = str(input())
    conj1.append(num)

for i in range(conjunto2):
    num = str(input())
    conj2.append(num)

for i in conj2:
    if i not in contados:
        uniao.append(i)
        contados.append(i)
for i in conj1:
    if i not in contados:
        uniao.append(i)
        contados.append(i)

print(uniao)

for i in conj1:
    for j in conj2:
        if i == j:
            intersecao.append(i)
print(intersecao)

for i in conj1:
    if i not in conj2:
        diferenca.append(i)

print(diferenca)