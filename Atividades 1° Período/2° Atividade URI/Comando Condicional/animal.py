a1 = str(input())
a2 = str(input())
a3 = str(input())

if a1 == 'vertebrado':
    if a2 == 'ave':
        if a3 == 'carnivoro':
            print("aguia")
        elif a3 == 'onivoro':
            print('pomba')
    elif a2 == 'mamifero':
        if a3 == 'onivoro':
            print("homem")
        elif a3 == 'herbivoro':
            print("vaca")

elif a1 == 'invertebrado':
    if a2 == 'inseto':
        if a3 == 'hematofago':
            print("pulga")
        elif a3 == 'herbivoro':
            print("lagarta")
    elif a2 == 'anelideo':
        if a3 == 'hematofago':
            print("sanguessuga")
        elif a3 == 'onivoro':
            print("minhoca")