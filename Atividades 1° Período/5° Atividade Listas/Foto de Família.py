n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

ordem_familia = []
ordem_familia.extend([n1, n2, n3, n4])
ordem_familia.sort()

print("{:.2f}".format(ordem_familia[0]))
print("{:.2f}".format(ordem_familia[2]))
print("{:.2f}".format(ordem_familia[3]))
print("{:.2f}".format(ordem_familia[1]))
