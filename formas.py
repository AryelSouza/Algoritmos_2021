fig = input()
pi = 3.14


if fig == "Q":
    tlq = float(input())
    aq = tlq * tlq
    pq = 4 * tlq
    print("{:.2f}".format(aq))
    print("{:.2f}".format(pq))
elif fig == "R":
    la = float(input())
    lr = float(input())
    aqr = la*lr
    pqr = la + la + lr + lr
    print("{:.2f}".format(aqr))
    print("{:.2f}".format(pqr))

elif fig == "C":
    r = float(input())
    ac = pi * r*2
    cpc = 2*pi*r
    print("{:.2f}".format(ac))
    print("{:.2f}".format(cpc))
else:
     print("Nenhuma figura selecionada")
