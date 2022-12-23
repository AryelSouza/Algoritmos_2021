numero=int(input())
for x in range(1,numero+1):
    numeros = ''
    for i in range(x):
        numeros += '{}'.format(x)
    print(numeros)