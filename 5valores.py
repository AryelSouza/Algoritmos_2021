x=0
numeros=0
while True:

    n=float(input())
    numeros+=1
    if n<0:

        x+=1
    print("Digite um valor:")
    if numeros==5:
        print("Foram digitados {} numeros negativos".format(x))
        break


