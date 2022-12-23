nota1=int(input())
nota2=int(input())
nota3=int(input())

media=float(nota1+nota2+nota3)/3

if media <0 or media >100:
    print("Media invalida")

if media >=70 and media <=100:
    print("A media do aluno foi {:.2f} e ele foi APROVADO".format(media))

if media >=40 and media <=70:
    print("A media do aluno foi {:.2f} e ele foi FINAL".format(media))
if media >=0 and media <=40:
    print("A media do aluno foi {:.2f} e ele foi REPROVADO".format(media))