raio = float(input())
angulo = float(input())

comp_do_arco = (3.14*raio*angulo)/180

print("{:.2f}".format(comp_do_arco))

area_do_setor = angulo*3.14*raio**2/360

print("{:.2f}".format(area_do_setor))