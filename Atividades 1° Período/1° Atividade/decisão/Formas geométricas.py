print("Bem-vindo, para selecionar uma forma geométrica digite 'Q' para quadrado, 'R' para retângulo e 'C' para círculo. ")
entrada_forma = str(input("Digite a forma: "))

if entrada_forma == 'Q':
    ladoQ = float(input("Digite quanto é o lado: "))
    areaQ = ladoQ ** 2
    periQ = 4 * ladoQ
    print("Essa é a área: {:.2f}".format(areaQ))
    print("Esse é o perímetro: {:.2f}".format(periQ))

elif entrada_forma == 'R':
    alturaR = float(input("Digite quanto é a altura: "))
    larguraR = float(input("Digite quanto é a largura: "))
    areaR = alturaR * larguraR
    periR = 2 * (alturaR + larguraR)
    print("Essa é a área: {:.2f}".format(areaR))
    print("Esse é o perímetro: {:.2f}".format(periR))

elif entrada_forma == 'C':
    raioC = float(input("Digite quanto é o raio"))
    areaC = 3.14 * (raioC ** 2)
    comp_circ = 2 * 3.14 * raioC
    print("Essa é a área: {:.2f}".format(areaC))
    print("Esse é o comprimento do círculo: {:.2f}".format(comp_circ))

else:
    print("Nenhuma figura selecionada")




