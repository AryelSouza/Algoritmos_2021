n=int(input())

for j in range(1, n):
    soma_div = 0

    for i in range(1, j+1):
        if j % i == 0:
            soma_div += i

    if soma_div == j*2:
        print(j)