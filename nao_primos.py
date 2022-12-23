x=int(input())

for i in range (1,x+1):

    eh_primo = True

    for j in range(2,i):
        if i % j == 0:
            eh_primo=False

    if not eh_primo or i ==1 :
         print(i,end=" ")