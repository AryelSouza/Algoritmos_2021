n = int(input())
numeros = 0
mult10 = False

for i in range(n):
    numeros += 1
    if numeros%10== 0:
        mult10 = True
    else:
        print(numeros)
        mult10 = False