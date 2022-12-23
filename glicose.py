# INICIA AS VARIÁVEIS COM VALORES VAZIOS
numero_de_entradas = 0
glicose_media = 0
glicose_dia = 0
glicose = 0

# OUTRA FORMA ALTERNATIVA DE INICIAR AS VARIÁVEIS COM ZERO:
# numero_de_entradas = glicose_media = glicose_dia = glicose = 0

# PEDE PARA O USUARIO DIGITAR A GLICOSE INFINITAMENTE (ATÉ 0 SER PRESSIONADO)
while True:
    glicose = int(input())  # RECEBE A GLICOSE

    # SE ELE DIGITAR ZERO O LOOP ENCERRA
    if glicose == 0:
        break  # ENCERRA O LOOP

    glicose_dia += glicose  # SOMA A GLICOSE DO DIA
    numero_de_entradas += 1  # INCREMENTA O NUMERO DE ENTRADAS EM CADA LOOP / CADA VEZ QUE ELE INFORMAR UM VALOR
    glicose_media = glicose_dia / numero_de_entradas  # CALCULA A MEDIA A CADA LOOP


# PRINTA APENAS QUANDO O LOOP TERMINAR
if glicose_media < 110:
    print("Glicose Normal")
elif glicose_media >= 200:
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")

# PROGRAMA ACABA/ENCERRA