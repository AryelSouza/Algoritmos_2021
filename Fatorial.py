#errado
while True:
    n = int(input())
    if n == -1:
        break
    fat = 1
    i=2
    while i <=n:
        fat = fat =i
        i = i +1
    print(fat)