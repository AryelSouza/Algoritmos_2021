descifrando2 = []
posisao=[]
letras=[]
quantide_pedacos= int(input())

for i in range(quantide_pedacos):
    pos, letra= input().split()
    pos = int(pos)
    letras.append(letra)
    posisao.append(pos)
    descifrando2.append(i)
descifrando2.append(19)

for x,y in zip(posisao,letras):
    descifrando2[x]= y
descifrando2.pop(0)

nome = ''
for count , i in enumerate(descifrando2):
    nome += i
print(nome)