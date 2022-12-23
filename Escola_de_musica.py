x=float(input())
y=int(input())

if x>=9.5 and y<=10:
    print("APROVADO COM LOUVOR")

elif x>=7 and x<9.5 and y<=10:
    print("APROVADO")

elif x<7:
    print("REPROVADO")

elif y>10:
    print("REPROVADO POR FALTAS")