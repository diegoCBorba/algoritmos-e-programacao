temperatura_paciente = float(input())
secrecao = str(input())

if secrecao == 'S':
        if temperatura_paciente >= 37:
                print("Exames Especiais")
        if temperatura_paciente < 37:
                print("Exames Basicos")

elif secrecao == 'N':
        if temperatura_paciente >= 37:
                print("Exames Basicos")
        if temperatura_paciente < 37:
                print("Liberado")

else:
        print("Erro")