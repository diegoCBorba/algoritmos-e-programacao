PSNR = int(input())

if 80 <= PSNR <= 90:
    enquadramento = str(input())
    exposicao = str(input())
    if enquadramento == 'bom' or enquadramento == 'excelente':
        if exposicao == 'bem exposta':
            print("para imprimir")

        elif exposicao == 'subexposta' or exposicao == 'superexposta':
            print("boa")

    else:
        print("marromeno")

if 50 <= PSNR < 80:
    enquadramento = str(input())
    exposicao = str(input())
    if enquadramento == 'excelente':
        if exposicao == 'bem exposta':
            print("boa")

    else:
        print("marromeno")

if PSNR < 50:
    enquadramento = str(input())
    exposicao = str(input())
    if enquadramento == 'excelente':
        if exposicao == 'bem exposta':
            print("marromeno")

        else:
            print("lixo")

    else:
        print("lixo")













