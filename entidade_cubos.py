n = int(input())
nivel = 1
qtde_cubos = 1

while True:
    if n >= qtde_cubos:
        n = n - qtde_cubos
    else:
        break
    nivel += 1
    qtde_cubos += nivel

print(nivel-1)