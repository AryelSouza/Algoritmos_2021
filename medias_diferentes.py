tipo_nota=str(input())
if tipo_nota != "a" and tipo_nota != "p" and tipo_nota != "h":
    print("Escolha um tipo de media valida.")
else:
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    media = 0


    if tipo_nota == "a":
        media = (nota1 + nota2 + nota3) / 3
    elif tipo_nota == "p":
        peso1 = int(input())
        peso2 = int(input())
        peso3 = int(input())
        media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
    elif tipo_nota == "h":
        media = 3/((1/nota1) + (1/nota2) + (1/nota3))

    if 70<= media <= 100:
        print(f"{media:.2f}")
        print("Aprovado")
    elif 0<= media <=40:
        print(f"{media:.2f}")
        print("Reprovado")
    elif 40< media <70:
        print(f"{media:.2f}")
        print("Final")
    else:
        print("Média inválida")