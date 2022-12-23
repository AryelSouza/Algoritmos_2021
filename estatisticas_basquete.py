jogos=int(input())
if jogos <=2:
    print('Jogador em avaliacao')
else:
    for x in range(jogos):
        soma_jgs = 0
        soma_rbt = 0
        soma_ast = 0
        s_rbt_o = 0
        s_rbt_d = 0
        s_mnt=0
        media_mnts=0
        soma_total=0
    for i in range(jogos):
        mnts=int(input())
        pont_feitos=int(input())
        rebote_of=int(input())
        rebote_def=int(input())
        assist=int(input())
        soma_jgs+=pont_feitos
        soma_rbt+=rebote_def
        soma_rbt+=rebote_of
        soma_ast+=assist
        s_rbt_o+=rebote_of
        s_rbt_d+=rebote_def
        s_mnt+=mnts
        media_jgs = soma_jgs / jogos
        media_rbt = soma_rbt / jogos
        media_ast = soma_ast / jogos
        media_rbt_o = s_rbt_o / jogos
        media_rbt_d = s_rbt_d / jogos
        media_p_jg = soma_jgs / s_mnt
    estrela=0
    estrela2=0
    if media_jgs > 20:
        estrela+= 1
    if media_rbt >=10:
        estrela += 1
    if media_ast >= 10:
        estrela += 1
    if media_p_jg >= 1:
        estrela2 += 1
    if media_rbt_o >= 5:
        estrela2 +=1
    if media_rbt_d >= 7:
        estrela2 += 1
    print("Pontos por jogo {:.2f}".format(media_jgs))
    print("Rebotes por jogo {:.2f}".format(media_rbt))
    print("Asistencias por jogo {:.2f}".format(media_ast))
    print("Pontos por minuto {:.2f}".format(media_p_jg))
    print("Rebotes ofensivos por jogo {:.2f}".format(media_rbt_o))
    print("Rebotes defensivos por jogo {:.2f}".format(media_rbt_d))
    if estrela >= 2:
        print("All-star")
    elif estrela and estrela2 >=1:
        print("Jogador titular")
    elif estrela == 1:
        print("Jogador de rotacao")
    elif estrela2 == 1:
        print("Jogador de banco")
    elif estrela == 0 and estrela2 == 0:
        print("Jogador em processo de dispensa")