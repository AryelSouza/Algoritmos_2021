quantidade=0
caixa=12

while True:
    prego=int(input())
    if prego % 2 == 1:
            break
    else:
        quantidade += prego
while caixa< quantidade:
    caixa+=caixa
restante=caixa-quantidade
preco_total=(caixa/12)*7.89
print('{:.2f}\n{}'.format(preco_total,restante))