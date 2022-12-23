dias = int(input())
km_t = int(input())
cota_km = dias * 100

if km_t < cota_km:
    total = dias * 90
else:
    total = (dias * 90) + ((km_t - cota_km) * 12)

print(f"{float(total):.2f}")