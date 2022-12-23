cont = 1
cont_princesa= 0

k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())

while cont <= d:
    if cont % i == 0 or cont % m == 0 or cont % n == 0 or cont % k == 0:
        cont_princesa += 1
    cont += 1
print(cont_princesa)