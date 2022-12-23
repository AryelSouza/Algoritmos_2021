dia_anterior=999
depositado=0
depositado_total=0
dias_metas=0
total=0 #total de entradas do programa


while total <=7:
    depositado=float(input())
    total +=1
    depositado_total = depositado_total + depositado
    if depositado > dia_anterior:
        dias_metas +=1
    dia_anterior=depositado
    depositado +=depositado

    if total ==7:
        print("R$ {:.2f}".format(depositado_total))
        print("{}".format(dias_metas))
        break