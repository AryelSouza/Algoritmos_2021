aluno_maior_media = ""
maior_media = 0

while True:

    while True: # Validação da nota da disciplina
        nota_disc = int(input())
        if 0 <= nota_disc <= 100:
            break

    if nota_disc == 0:
        break

    nome = input()
    horas = int(input())
    if nota_disc < 70 or horas < 8:
        print("Aluno NAO pode concorrer.")
    else:
        cre = int(input())

        while True: # Validação da nota da prova
            nota_prova = int(input())
            if 0 <= nota_prova <= 100:
                break
        if nota_prova < 70:
            print("Aluno reprovado na prova de monitoria!")
        else:
            nota_final = nota_disc * 0.4 + cre * 0.1 + nota_prova * 0.5
            if nota_final >= 70 and nota_final > maior_media:
                maior_media = nota_final
                aluno_maior_media = nome

            if nota_final >= 70:
                print("Aluno aprovado! Sua media foi {:.2f}.".format(nota_final))
            else:
                print("Aluno reprovado na selecao. Media= {:.2f}.".format(nota_final))

if aluno_maior_media == "":
    print("Resultado da monitoria: Sem alunos aprovados.")
else:
    print("Resultado da monitoria: {}, {:.2f}.".format(aluno_maior_media, maior_media))