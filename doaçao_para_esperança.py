doacoes = 0
doacoes_futuras = 0

while True:
    doacao = int(input())

    if doacao < 1: # Saída do laço
        break
    # else

    while True: # Validacao da opção
        opcao = int(input())
        if opcao == 1 or opcao == 2:
            break
        print("Valor invalido")

    doacoes += doacao
    if opcao == 2:
        while True:  # Validacao da quantidade de meses
            meses = int(input())
            if 2 <= meses <= 12:
                break
            print("Favor digitar valor entre 2 e 12, inclusive")
        doacoes_futuras += doacao*(meses-1)

print("Total arrecadado para agora: R$ {:.2f}".format(doacoes))
print("Total arrecadado para meses futuros: R$ {:.2f}".format(doacoes_futuras))