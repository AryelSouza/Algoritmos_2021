par=int(input())
pts=int(input())
qtde_convidados = 0
for i in range(par):
    nota1=int(input())
    nota2=int(input())
    if nota1+nota2>=pts and nota1>0 and nota2>0:
        qtde_convidados+=1

print(qtde_convidados)