l = ["T", "A", "C", "G"]

conv = ["A", "T", "G", "C"]


q = int(input())

for _ in range(q):
    pri = input()
    seg = input()
    con = ""

    for i, letra in enumerate(pri):
        x = conv.index(letra)
        con += l[x]


    if con == seg:
        print("COMPLEMENTARES")


    else:
        print("NAO COMPLEMENTARES")
        print(con)