velocidade = int(input())
multa = 0

if velocidade > 50:
    if velocidade > 50:
        multa = 230.00
    if velocidade > 55:
        multa = 340.00
    if velocidade > 60:
        s = velocidade - 50
        multa = s * 19.28

print("{:.2f}".format(multa))