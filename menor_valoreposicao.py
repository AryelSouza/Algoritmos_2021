tamanho=int(input())
numeros=input().split()
print('Menor valor: {}'.format(min(numeros)))
print('Posicao: {}'.format(numeros.index(min(numeros))))