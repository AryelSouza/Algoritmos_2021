peso=0
moch=0
while True:
    livro=int(input())
    peso+= livro
    if peso > 18:
        break
    elif peso < 18:
        moch+=1
print(moch)