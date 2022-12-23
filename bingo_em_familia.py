ganhador = ""
cart_ambrosinha = []
cart_ambrosio = []
cart_ambrosio_jr = []
noms = []
menor = 17

sorts = list(map(int, input().split()))

def verifik_gan(cart, bolas, men):
    corretas = 0
    for k in range(3):
        for l in range(3):
            for b in range(16-(15-men)):
                if cart[k][l] == bolas[b]:
                    corretas += 1
                    break
    return corretas

def cartelas(ctl):
    noms.append(input())
    for j in range(3):
        ctl.append([])
        ctl[j] = list(map(int, input().split()))

def verifik_primeiro(cart, bolas):
    corretas = 0
    maior = 0
    for k in range(3):
        for l in range(3):
            for b in range(len(bolas)):
                if cart[k][l] == bolas[b]:
                    if maior < bolas.index(bolas[b]):
                        maior = bolas.index(bolas[b])
                    corretas += 1
                    if corretas == 9:
                        return maior
                    break
    return 16

cartelas(cart_ambrosinha)
cartelas(cart_ambrosio)
cartelas(cart_ambrosio_jr)

num_ambrosinha = verifik_primeiro(cart_ambrosinha, sorts)
num_ambrosio = verifik_primeiro(cart_ambrosio, sorts)
num_ambrosio_jr = verifik_primeiro(cart_ambrosio_jr, sorts)

if menor > num_ambrosinha:
    menor = num_ambrosinha
    ganhador = noms[0]
if menor > num_ambrosio:
    menor = num_ambrosio
    ganhador = noms[1]
if menor > num_ambrosio_jr:
    menor = num_ambrosio_jr
    ganhador = noms[2]

print("{} GANHOU!!".format(ganhador.upper()))
print("Ambrosinha: {} numeros sorteados".format(verifik_gan(cart_ambrosinha, sorts, menor)))
print("Ambrosio: {} numeros sorteados".format(verifik_gan(cart_ambrosio, sorts, menor)))
print("Ambrosio Junior: {} numeros sorteados".format(verifik_gan(cart_ambrosio_jr, sorts, menor)))