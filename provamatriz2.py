lin = int(input("Digite a quantidade de linhas da matriz: "))
while lin < 1:
    lin = int(input("Não dá para fazer uma matriz com 0 linhas,digite novamente: "))
c = int(input("Digite a quantidade de colunas da matriz: "))
while c < 1:
    c = int(input(f"Não dá para fazer uma matriz com {lin} linhas e 0 colunas,digite novamente: "))
def numero_lista():
    nums = []
    for i in range(len(mat)):
        for col in range(len(mat[i])):
            n = mat[i][col]
            nums.append(n)
    return nums
def contador_repetidos(a):
    for i in range(max(a)+1):
        rep = a.count(i)
        if rep >= 2:
            print("{}:{}".format(i, rep))

mat = []

for linha in range(lin):
    mat.append([])
    for coluna in range(c):
        lin = int(input("Digite os numeros da matriz um por vez: "))

        mat[linha].append(lin)
junt =numero_lista()
contador_repetidos(junt)