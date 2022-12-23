ia = int(input())

if ia <= 18:
    print("Não pode adotar")
elif ia > 18:
    irm = str(input())
    ac = str(input())
    sit = str(input())
    ic = int(input())
    pais = str(input())
    cp = str(input())
    cc = str(input())

    if ia - ic < 16 or irm == "S":
        print("Não pode adotar")
    elif ia > 18 and ia - ic >= 16 and irm == "N":
        if (ac == "S" and sit == "S") or (ac == "N" and sit == "N") or (ac == "N" and sit == "S"):
            if (pais == "S" and cp == "N") or (pais == "S" and cp == "S") or (pais == "N" and cp == "S"):
                if (ic <= 12 and cc == "N") or (ic <= 12 and cc == "S") or (ic > 12 and cc == "S"):
                    print("Pode adotar")
                else:
                    print("Não pode adotar")
            else:
                print("Não pode adotar")
        else:
            print("Não pode adotar")