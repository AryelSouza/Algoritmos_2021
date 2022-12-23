x=int(input())

n1=0
n2=0
n3=0
for i in range(1,x):
    n1=i
    n2=i+1
    n3=i+2
    if x==(n1*n2*n3):
     print("{} * {} * {} = {}".format(n1,n2,n3,x))
     print("Verdadeiro")
     break
else:
    print("Falso")