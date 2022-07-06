salario = float(input())

p1 = 1.15 #0 - 400.00
p2 = 1.12 #400.01 - 800.00
p3 = 1.1 #800.01 - 1200.00
p4 = 1.07 #1200.01 - 2000.00
p5 = 1.04 #Acima de 2000.00

if 0 <= salario <= 400:
    sTotal = salario * p1
    reajuste = salario * 0.15
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(sTotal, reajuste))

elif 400 < salario <= 800:
    sTotal = salario * p2
    reajuste = salario * 0.12
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(sTotal, reajuste))

elif 800 < salario <= 1200:
    sTotal = salario * p3
    reajuste = salario * 0.1
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(sTotal, reajuste))

elif 1200 < salario <= 2000:
    sTotal = salario * p4
    reajuste = salario * 0.07
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(sTotal, reajuste))

elif salario > 2000:
    sTotal = salario * p5
    reajuste = salario * 0.04
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(sTotal, reajuste))


