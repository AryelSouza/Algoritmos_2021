n = int(input())

a1 = []
a2 = []

for i in range(n):
    elem = int(input())
    a1.append(elem)

for i in range(n):
    elem = int(input())
    a2.append(elem)

for i in range(n):
    print(a1[i])
    print(a2[i])