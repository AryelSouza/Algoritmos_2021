num = int(input())

if num >= 2:

    for i in range(num + 1):
        prm = False

        for x in range(2, i):
            if i % x == 0:
                prm = True


        if not prm and i != 1 and i!= 0:
            print(i)
elif num <= 1:
    print("Sem numeros primos no intervalo informado.")