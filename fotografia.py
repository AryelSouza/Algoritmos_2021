psnr = int(input())
enquadramento = input()
exposicao = input()

if 80 <= psnr <= 90:
    if enquadramento == "bom" or enquadramento == "excelente" and exposicao == "bem exposta":
        print("para imprimir")
    elif enquadramento == "bom" or enquadramento == "excelente" and exposicao == "subexposta" or exposicao == "superexposta":
        print("boa")
    else:
        print("marromeno")

if 50 <= psnr < 80:
    if enquadramento == "excelente" and exposicao == "bem exposta":
        print("boa")
    else:
        print("marromeno")

if psnr < 50:
    if enquadramento == "excelente" and exposicao == "bem exposta":
        print("marromeno")
    else:
        print("lixo")