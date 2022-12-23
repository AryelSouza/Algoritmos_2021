frase = input().split()

# ['Odd', 'Word', 'Problem']
#    1       2          3
#    0       1          2

for i in range(1, len(frase), 2):
    frase[i] = frase[i][::-1]

for i in range(len(frase)):
    print(frase[i], end= " ")
