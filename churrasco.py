CBA = 0.2 #Carne bovina por adulto em Kilogramas
CFA = 0.1 #Carne de frango por adulto em kg
CSA = 0.1 #Carne de frango por adulto em kg
CBC = 0.2 #Carne bovina por criança em kg



PB = 32#Preço da carne bovina
PF = 18#Preço da carne de frango
PS = 15#Preço da carne suina
PCERVA = 8#Preço da cerveja
PREFRI = 6#Preço do refrigerante
QGCA= 2 #Quantidade de garrafas de cerveja por adulto
QRC = 0.5 #Quantidade de garrafas de refrigerante por criança
DESC2 = 0.98#Desconto de 2%

COMPLETO = "C"
BOVINO_FRANGO = "BF"
BOVINO_SUINO = "BS"

tipo_churra = input()

if tipo_churra != "C" and tipo_churra != "BF" and tipo_churra != "BS":
    print("Opção inválida")
else:


    pao_alho = input()
    bebidas_adultos = input()
    bebidas_criancas = input()
    q_c = int(input())  # quantidade de crianças
    q_a = int(input())  # quantidade de adultos

    if tipo_churra == "C":
        valor_total = q_a*CBA*PB + q_a*CFA*PF + q_a*CSA*PS + q_c*CBC*PB
    if pao_alho =="N":
        valor_total = valor_total * DESC2
        # valor_total *= DESC2
    if bebidas_adultos == "S":
        valor_total = valor_total + 2*PCERVA*q_a
         # Valor_total += 2 * PCERVA * q_a
    if bebidas_criancas == "S":
        valor_total = valor_total + 0.5 * PREFRI * q_a
         # valor_total +=0.5 * PREFRI * q_a

print(valor_total)