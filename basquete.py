time = str(input())

if time != "GSW" and time != "HOU" and time != "CLE" and time != "BOS":
    print("Nenhum time de interesse jogando.")
else:

    # principais:
    jogador = str(input())
    arremessos_tentados_2pts = int(input())
    arremessos_convertidos_2pts = int(input())
    arremessos_tentados_3pts = int(input())
    arremessos_convertidos_3pts = int(input())

    # constantes:
    pontos2 = (arremessos_convertidos_2pts *2)
    pontos3 = (arremessos_convertidos_3pts *3)
    q_arremessos2 = arremessos_tentados_2pts + arremessos_convertidos_2pts
    q_arremessos3 = arremessos_tentados_3pts + arremessos_convertidos_3pts

    # derivadas:
    pontos_totais = pontos2 + pontos3
    percentual_2pts = (arremessos_convertidos_2pts/ arremessos_tentados_2pts)*100
    percentual_3pts = (arremessos_convertidos_3pts/ arremessos_tentados_3pts)*100

    if pontos_totais > 30 or (percentual_2pts > 50.0 and q_arremessos2 > 10) or (percentual_3pts > 40.0 and q_arremessos3 > 7):
        print("O time {} estah jogando, e {} estah indo bem.".format(time, jogador))
    else:
        print("O time {} estah jogando, mas {} nao estah indo bem.".format(time, jogador))