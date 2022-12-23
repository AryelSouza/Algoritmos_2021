d1 = int(input())
co, re, de = input().split()
co = float(co)
re = float(re)
de = float(de)

d2 = int(input())
coa, rea, cea, dea = input().split()
coa = float(coa)
rea = float(rea)
cea = float(cea)
dea = float(dea)


if 1 <= d1 <= 24:
    if d1 < 20:
        re = re - (re * 0.10)
        de = de - (de * 0.15)
    elif d1 == 20:
        co = co - (co * 0.12)
        re = re - (re * 0.15)
        de = de - (de * 0.20)
    elif d1 == 21:
        co = co - (co * 0.17)
        re = re - (re * 0.22)
        de = de - (de * 0.27)
    elif d1 == 22:
        co = co - (co * 0.20)
        re = re - (re * 0.22)
        de = de - (de * 0.30)
    elif d1 == 23:
        co = co - (co * 0.25)
        re = re - (re * 0.29)
        de = de - (de * 0.35)
    elif d1 == 24:
        co = co - (co * 0.35)
        re = re - (re * 0.35)
        de = de - (de * 0.50)
    else:
        print("Tente novamente!")

    natal = co + re + de

else:
    print("Tente novamente.")

if 25 <= d2 <= 31:
    if d2 == 25:
        coa = coa - (coa * 0.15)
        rea = rea - (rea * 0.13)
        dea = dea - (dea * 0.10)
    elif d2 == 26:
        coa = coa - (coa * 0.19)
        rea = rea - (rea * 0.25)
        cea = cea - (cea * 0.05)
        dea = dea - (dea * 0.23)
    elif d2 == 27:
        coa = coa - (coa * 0.24)
        rea = rea - (rea * 0.30)
        cea = cea - (cea * 0.12)
        dea = dea - (dea * 0.33)
    elif d2 == 28:
        coa = coa - (coa * 0.30)
        rea = rea - (rea * 0.32)
        cea = cea - (cea * 0.20)
        dea = dea - (dea * 0.35)
    elif d2 == 29 or d2 == 30:
        coa = coa - (coa * 0.35)
        rea = rea - (rea * 0.40)
        cea = cea - (cea * 0.33)
        dea = dea - (dea * 0.42)
    elif d2 == 31:
        coa = coa - (coa * 0.40)
        rea = rea - (rea * 0.47)
        cea = cea - (cea * 0.45)
        dea = dea - (dea * 0.66)
    else:
        print("Tente novamente!")

    ano_novo = coa + rea + cea + dea

else:
    print("Tente novamente!")


total = natal + ano_novo

print("Compras de natal: R$ {:.2f}.".format(natal))
print("Compras de ano novo: R$ {:.2f}.".format(ano_novo))
print("Total das compras: R$ {:.2f}.".format(total))