def pprint(entrada):
    saida = ''
    for l in entrada:
        for c in l:
            saida += str(c)
        saida += "\n"
    print(saida)
def pintada(mandala, i, j, c):
    if i >= 0 and i < n and j >= 0 and j < m and mandala[i][j] != '#':
        if mandala[i][j] != c:
            mandala[i][j] = c
            pintada(mandala, i - 1, j, c)
            pintada(mandala, i + 1, j, c)
            pintada(mandala, i, j - 1, c)
            pintada(mandala, i, j + 1, c)
n, m = map(int, input().split())
mandala = [[0] * n for i in range(m)]
for i in range(n):
    linha = input()
    for c in range(len(linha)):
        mandala[i][c] = linha[c]
t = int(input())
for p in range(t):
    i, j, c = map(int, input().split())
    pintada(mandala, i, j, c)
    pprint(mandala)