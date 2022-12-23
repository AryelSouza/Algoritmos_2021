n = int(input())


numerador = 1
denominador = 3

s = 0
termos= ""

for i in range(1, n+1):

    s += numerador/denominador
    termos += "{}/{}".format(numerador, denominador)
    numerador += 1
    denominador += 3

    if i < n:
        termos += " + "

print(termos)
print("{:.2f}".format(s))