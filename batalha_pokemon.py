from math import ceil

batalhas = int(input())

for b in range(batalhas):
    vc, vb, dc, db = map(int, input().split())
    while True:
        rb = ceil(vc / db)
        rc = ceil(vb / dc)

        if rc <= rb:
            print("Clodes")
            break

        if vc <=0:
            print("Bezaliel")
            break

        dc +=50
        vc -=db