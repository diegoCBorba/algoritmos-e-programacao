valor = int(input())

nota100 = valor//100
nota50 = (valor%100)//50
nota20 = ((valor%100)%50)//20
nota10 = (((valor%100)%50)%20)//10
nota5 = ((((valor%100)%50)%20)%10)//5
nota2 = (((((valor%100)%50)%20)%10)%5)//2
nota1 = (((((valor%100)%50)%20)%10)%5)%2

print(valor)
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))
