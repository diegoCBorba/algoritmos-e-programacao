
pacote = int(input())
pagamento = str(input())

if pacote == 1:
    if pagamento == "d" or pagamento == "D":
        print("Valor contratado= R$ 76.76\nQuantidade de canais= 38")
    elif pagamento == "c" or pagamento == "C" or pagamento == "a" or pagamento == "A":
        print("Valor contratado= R$ 80.80\nQuantidade de canais= 32")
    else:
        print("Forma de pagamento invalida.")

elif pacote == 2:
    if pagamento == "d" or pagamento == "D":
        print("Valor contratado= R$ 95.38\nQuantidade de canais= 61")
    elif pagamento == "c" or pagamento == "C" or pagamento == "a" or pagamento == "A":
        print("Valor contratado= R$ 100.40\nQuantidade de canais= 55")
    else:
        print("Forma de pagamento invalida.")

elif pacote == 3:
    if pagamento == "d" or pagamento == "D":
        preco3 = 130.23 * 0.90
        print("Valor contratado= R$ {:.2f}\nQuantidade de canais= 81".format(preco3))
    elif pagamento == "c" or pagamento == "C" or pagamento == "a" or pagamento == "A":
        print("Valor contratado= R$ 130.23\nQuantidade de canais= 70")
    else:
        print("Forma de pagamento invalida.")

elif pacote == 4:
    if pagamento == "d" or pagamento == "D":
        preco3 = 130.23 * 0.90
        print("Valor contratado= R$ 193.95\nQuantidade de canais= 123".format(preco3))
    elif pagamento == "c" or pagamento == "C" or pagamento == "a" or pagamento == "A":
        print("Valor contratado= 215.50R$ \nQuantidade de canais= 112")
    else:
        print("Forma de pagamento invalida.")

else:
    print("Pacote selecionado invalido.")
