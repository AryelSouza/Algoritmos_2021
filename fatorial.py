def fatorial(n): # iterativo
    f = 1
    for i in range(n, 0, -1)
        f = f * i
    return f

def fatorial_rec(n): # recursivo
    return n * fatorial_rec(n-1)


print(fatorial(6))