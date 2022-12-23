linha=(input('informe o numero de linhas :'))
coluna = (input('agora o numero de colunas :'))
matriz = []
if linha<= 0 or coluna<=0:
    print('não se da para ter uma matriz sem elementos!')
else:
    print('pronto agora informe os elementos um por linha :')
    for x in range(linha):
        matriz.append([])
        for j in range(coluna):
            elementos = input()
            matriz[x].append(elementos)
    iguais = []
    for x in range(len(matriz)):
        for i in range(len(matriz[x])):
            achou = matriz[x][i]
            iguais.append(achou)
    for x in iguais:
        repetidos = iguais.count(x)
    if repetidos >= 2:
        print("{}:{}".format(x, repetidos))