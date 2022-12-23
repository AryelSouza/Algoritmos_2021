while True:
    ph = float(input())
    if ph == -1:
        break
    if ph < 7:
        print("ACIDA")
    elif ph > 7:
        print("BASICA")
    elif ph == 7:
        print("NEUTRA")