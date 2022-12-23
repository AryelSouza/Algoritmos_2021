divida = int(input())
parcela = int (input())

while divida > 0:
    print("(antes) {}".format(divida))
    divida = divida - parcela
    if divida < 0:
        divida = 0
    print("(depois) {}".format(divida))