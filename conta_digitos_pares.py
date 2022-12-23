def conta_dig_pares(n):
    if int(n[0]) % 2 == 0:
        return 1 + conta_dig_pares(n[1::])
