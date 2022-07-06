valor = float(input())
valor += 0.001
nota100 = valor//100
nota50 = (valor%100)//50
nota20 = ((valor%100)%50)//20
nota10 = (((valor%100)%50)%20)//10
nota5 = ((((valor%100)%50)%20)%10)//5
nota2 = (((((valor%100)%50)%20)%10)%5)//2
moeda1 = (((((valor%100)%50)%20)%10)%5)%2//1
moeda05 = ((((((valor%100)%50)%20)%10)%5)%2)%1//0.5
moeda025 = (((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5//0.25
moeda010 = ((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25//0.10
moeda005 = (((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10//0.05
moeda001 = ((((((((((valor%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10)%0.05//0.01

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ "
      "10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00".format(nota100, nota50, nota20, nota10, nota5,
                                                                           nota2))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ "
      "0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01".format(moeda1, moeda05, moeda025, moeda010,
                                                                            moeda005, moeda001))
