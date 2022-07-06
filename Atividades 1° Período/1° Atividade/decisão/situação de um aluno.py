nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3)/ 3

if media >= 70 and media <= 100:
    print("A media do aluno foi {:.2f} e ele foi APROVADO".format (media))

elif media >= 0 and media <= 40:
    print("A media do aluno foi {:.2f} e ele foi REPROVADO".format(media))

elif media > 40 and media < 70:
    print("A media do aluno foi {:.2f} e ele foi FINAL".format(media))

else:
    print("Media invalida")


