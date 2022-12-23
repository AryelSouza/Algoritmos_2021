num_pessoas=0
peso_pessoas=0

while num_pessoas <7 and peso_pessoas <560:
    peso=float(input())
    if peso==0:
        break
    peso_pessoas +=peso
    num_pessoas +=1

print(num_pessoas)
print(peso_pessoas)