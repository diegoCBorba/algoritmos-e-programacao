"""
lista = []

while True:
    n = str(input())
    if n == "-1":
        break
    lista.append(n)

nome = str(input())
nome_l = list(nome)

if nome_l in lista:
    print("Nome está na lista")
else:
    print("Nome não está na lista")

"""

lista = []
count = 0

while True:
    n = str(input())
    if n == "-1":
        break
    lista.append(n)

nome = str(input())
nome_l = list(nome)

for i in nome_l:
    if i in lista:
        count += 1

if count == len(nome_l):
    print("Nome pode ser criado na lista")
else:
    print("Nome não pode ser criado na lista")