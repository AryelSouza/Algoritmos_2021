qtde_dias_meta = 0
soma = 0

for i in range(7):
    cartas = int(input())
    if cartas >= 100:
        qtde_dias_meta +=1
    soma += cartas

print(qtde_dias_meta)
print(soma//7)