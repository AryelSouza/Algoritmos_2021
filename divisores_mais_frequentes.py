x = int(input())

n = 0
d = 0

for i in range(2,x):
    temp = x
    divisao = 0
    while temp % i == 0:
        temp = temp / i
        divisao +=1

    if divisao > n:
        n = divisao
        d = i
print("mostFrequent: {}, frequency: {}".format(d, n))