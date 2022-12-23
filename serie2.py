n = int(input())

numerador = 1
denominador = 4
s=0
termos=""

for i in range(n):
    if i % 2 == 0:
        s += numerador/denominador
        termos += "{}/{}".format(numerador,denominador)
        numerador += 2
        denominador +=4
    else:
        s +=1
        termos +="1"

    if i < n-1:
        termos +=" + "
print("{:.2f}".format(s))
print(termos)