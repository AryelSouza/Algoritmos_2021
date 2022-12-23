cin = 0
bol = 0
total = 0
escolha = input()
escolha = escolha.lower()


while (escolha == "cinema" or escolha == "boliche"):
    if escolha == "cinema":
        cin += 1
    elif escolha == "boliche":
        bol += 1
    total= cin + bol
    if total == 6:
        if cin > bol:
            print("CINEMA")
            break
        elif cin == bol:
            print("BOLICHE")
            break
        elif bol > cin:
            print("BOLICHE")
            break

    else:
        escolha = input()
        escolha = escolha.lower()