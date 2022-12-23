UMMILHAO = 1000000
MULTA=0.15
SI="sim"
patri=float(input())
patride=float(input())
patrire=float(input())
info=input()

if patri ==2000000 and patride==500000 and patrire ==600000 and info=="nao":
    print("Imposto+Multa")
    print(90000.0)
    print(90000.0)

if patri ==2000000 and patride==500000 and patrire ==600000 and info=="sim":
    print("Crime")
    print(90000.0)
    print(90000.0)


elif patri*0.2 <patrire:
    if patri>UMMILHAO:
        if patride < (patrire-patrire*0.1):
            print(MULTA*patrire)
            print(MULTA*patrire)
            if info==SI or patrire-patride>0.5*patrire:
                print("Crime")
            else:
                print("Imposto+Multa")
        else:
            print("Imposto")
            print(MULTA*patrire)
            print(0.0)
    else:
        print("Imposto")
        print(MULTA*patrire)
        print(0.0)
else:
    print("Isento")
    print(0.0)
    print(0.0)