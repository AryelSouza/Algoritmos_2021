soma = 0
qtde_jog = 0
maior_pts = 0
maior_pts_jogador = ""

menor_pts = 9999999999999999999
menor_pts_jogador=""

while True:
    nome = input()
    if nome == "sair":
        break
    pts = int(input())

    if pts>=maior_pts:
        maior_pts=pts
        maior_pts_jogador=nome
    if pts <= menor_pts:
        menor_pts = pts
        menor_pts_jogador=nome
    soma += pts
    qtde_jog +=1
if maior_pts_jogador=="":
    print("Nenhum jogador foi registrado.")
else:
    print(menor_pts_jogador)
    print(maior_pts_jogador)
    print("{:.2f}".format(soma/qtde_jog))

