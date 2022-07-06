n1, n2, n3, n4 = map(float, input().split())

mediaP = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/10

if mediaP >= 7:
    print("Media: {:.1f}".format(mediaP))
    print("Aluno aprovado.")

elif mediaP < 5:
    print("Media: {:.1f}".format(mediaP))
    print("Aluno reprovado.")

elif 5 <= mediaP < 7:
    notaEx = float(input())
    total = (notaEx + mediaP)/2
    print("Media: {:.1f}".format(mediaP))
    print("Aluno em exame.")
    print("Nota do exame: {:.1f}".format(notaEx))
    if total >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(total))
    elif total < 5:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(total))