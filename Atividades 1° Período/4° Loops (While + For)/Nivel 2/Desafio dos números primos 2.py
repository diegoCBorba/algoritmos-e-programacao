soma_primos = 0
n1 = int(input())

while True:
    n2 = int(input())

    if n2 <= n1:
        print("Digite um valor maior que o primeiro!")
    else:
        break

for i in range (n1, n2 + 1):
    if i == 2 or i == 3 or i == 5 or i == 7:
        soma_primos += i
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        soma_primos += i

if soma_primos == 0:
    print("Sem numeros primos no intervalo informado.")

else:
    print(soma_primos)



