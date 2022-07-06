
D1 = int(input())
CO, RE, DE = map(float, input().split())
D2 = int(input())
CO1, RE1, CE, DE1 = map(float, input().split())

if D1 < 20:
    valorRE = RE * 0.90
    valorDE = DE * 0.85
    totalD1 = valorDE + valorRE + CO

if D1 == 20:
    valorCO = CO * 0.88
    valorRE = RE * 0.85
    valorDE = DE * 0.80
    totalD1 = valorDE + valorRE + valorCO

if D1 == 21:
    valorCO = CO * 0.83
    valorRE = RE * 0.78
    valorDE = DE * 0.73
    totalD1 = valorDE + valorRE + valorCO

if D1 == 22:
    valorCO = CO * 0.80
    valorRE = RE * 0.78
    valorDE = DE * 0.70
    totalD1 = valorDE + valorRE + valorCO

if D1 == 23:
    valorCO = CO * 0.75
    valorRE = RE * 0.71
    valorDE = DE * 0.65
    totalD1 = valorDE + valorRE + valorCO

if D1 == 24:
    valorCO = CO * 0.65
    valorRE = RE * 0.65
    valorDE = DE * 0.50
    totalD1 = valorDE + valorRE + valorCO

if D2 == 25:
    valorCO1 = CO1 * 0.85
    valorRE1 = RE1 * 0.87
    valorDE1 = DE1 * 0.90
    totalD2 = valorCO1 + valorRE1 + CE + valorDE1

if D2 == 26:
    valorCO1 = CO1 * 0.81
    valorRE1 = RE1 * 0.75
    valorCE = CE * 0.95
    valorDE1 = DE1 * 0.77
    totalD2 = valorCO1 + valorRE1 + valorCE + valorDE1

if D2 == 27:
    valorCO1 = CO1 * 0.76
    valorRE1 = RE1 * 0.70
    valorCE = CE * 0.88
    valorDE1 = DE1 * 0.67
    totalD2 = valorCO1 + valorRE1 + valorCE + valorDE1

if D2 == 28:
    valorCO1 = CO1 * 0.70
    valorRE1 = RE1 * 0.68
    valorCE = CE * 0.80
    valorDE1 = DE1 * 0.65
    totalD2 = valorCO1 + valorRE1 + valorCE + valorDE1

if D2 == 29 or D2 == 30:
    valorCO1 = CO1 * 0.65
    valorRE1 = RE1 * 0.60
    valorCE = CE * 0.67
    valorDE1 = DE1 * 0.58
    totalD2 = valorCO1 + valorRE1 + valorCE + valorDE1

if D2 == 31:
    valorCO1 = CO1 * 0.60
    valorRE1 = RE1 * 0.53
    valorCE = CE * 0.55
    valorDE1 = DE1 * 0.34
    totalD2 = valorCO1 + valorRE1 + valorCE + valorDE1

total = totalD1 + totalD2
print("Compras de natal: R$ {:.2f}.".format(totalD1))
print("Compras de ano novo: R$ {:.2f}.".format(totalD2))
print("Total das compras: R$ {:.2f}.".format(total))

