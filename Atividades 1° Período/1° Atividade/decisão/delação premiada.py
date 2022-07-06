print("Crimes possíveis: roubo, tráfico e domicídio.")
crime_delatador = str(input("Fale qual foi o crime do delatador: "))

if crime_delatador == 'roubo':
    valor_crime_delatador = int(input("Fale o valor do crime do delatador: "))
    delatado = str(input("Fale qual foi o crime da pessoa delatada: "))
    if delatado == 'homicídio':
        print("Delação concedida.")

    elif delatado == 'roubo':
        valor_delatado = int(input("Fale o valor do crime da pessoa delatada: "))

        if valor_delatado > (5 * valor_crime_delatador):
            print("Delação concedida.")

        else:
            print("Delação rejeitada.")

    elif delatado == 'tráfico':
        valor_delatado = int(input("Fale o valor do crime da pessoa delatada: "))
        if valor_delatado > (3 * valor_crime_delatador):
            print("Delação concedida.")

        else:
            print("Delação rejeitada.")

    else:
        print("Crime inválido.")

elif crime_delatador == 'tráfico':
    valor_crime_delatador = int(input("Fale o valor do crime do delatador: "))
    delatado = str(input("Fale qual foi o crime da pessoa delatada: "))
    if delatado == 'homicídio':
        print("Delação concedida.")

    elif delatado == 'roubo':
        print("Delação rejeitada.")

    elif delatado == 'tráfico':
        valor_delatado = int(input("Fale o valor do crime da pessoa delatada: "))
        if valor_delatado > (5 * valor_crime_delatador):
            print("Delação concedida.")

        else:
            print("Delação rejeitada.")
    else:
        print("Crime inválido.")

elif crime_delatador == "homicídio":
    delatado = str(input("Fale qual foi o crime da pessoa delatada: "))
    if delatado == 'homicídio':
        print("Delação concedida.")

    elif delatado == 'roubo':
        print("Delação rejeitada.")

    elif delatado == 'tráfico':
        print("Delação rejeitada.")

    else:
        print("Crime inválido.")

else:
    print("Crime inválido.")