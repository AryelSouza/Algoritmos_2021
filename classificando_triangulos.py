entrada = input()

while entrada != "FIM":
    l1, l2, l3 = map(int, entrada.split())
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        # Verifica se é isósceles, equilátero ou escaleno
        if l1 == l2 == l3:
            print("EQUILATERO")
        elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
            print("ISOSCELES")
        elif l1 != l2 != l3 or l1 != l3 != l2 or l3 != l2 != l1:
            print("ESCALENO")
    else:
        print("INVALIDO")
    entrada = input()