pop_inicial = int(input())
ano_inicial = int(input())
perc_cres = int(input())
ano_final = int(input())
ano_cresc = {}
taxa_cresc = pop_inicial
ano_cresc[ano_inicial] = pop_inicial

for i in range(ano_inicial+1, ano_final+1):
    taxa_cresc *= ((perc_cres/100) + 1)
    ano_cresc[i] = taxa_cresc

for ano, cresc in ano_cresc.items():
    print('{:.0f} {:.0f}'.format(ano, cresc))
