def mltpl(num):
    if num % 3 == 0:
        return True
    return False
def fat(num):
    fat = 1
    for x in range(2, num + 1):
        fat *= x
    return fat
def calc_som(num):
    soma = 0
    for u in range(num + 1):
        soma += (num / fat(u))
    return soma
resultados = 0
for s in range(5):
    numero = int(input())
    if mltpl(numero):
        resultados += fat(numero)
    else:
        resultados += calc_som(numero)
print("{:.2f}".format(resultados))