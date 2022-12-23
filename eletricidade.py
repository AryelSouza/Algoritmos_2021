kon = 9 * 10 ** 9
x1 = float(input())
x2 = float(input())
dist = float(input())

if dist > 0:
    forc = kon*(x1 * x2) / dist ** 2
    print(forc)
elif dist <= 0:
    print('Valor incorreto de distância')