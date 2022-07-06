dias = int(input())

idadeAno = dias // 365
idadeMeses = (dias % 365)//30
idadeDias = (dias % 365) % 30

print("{} ano(s)".format(idadeAno))
print("{} mes(es)".format(idadeMeses))
print("{} dia(s)".format(idadeDias))

