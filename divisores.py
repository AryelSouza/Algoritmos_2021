n = int(input())
numeros = 0
divisor = False

for i in range(n):
    numeros += 1
    if n%numeros== 0:
        print(numeros)
        divisor = True
    else:

        divisor = False