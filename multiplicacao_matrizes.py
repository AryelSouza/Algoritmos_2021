n, m, o = map(int, input().split())

def preenche_matriz(matriz, l):
    for l in range(l):
        matriz.append(list(map(int, input().split())))

m_a = []
preenche_matriz(m_a, n)

m_b = []
preenche_matriz(m_b, n)

matriz_mult = []
for l in range(n+1):
    elem = 0
    for c in range(o+1):
        elem += m_a[l][c] *m_b[c][l]
    matriz_mult.append(elem)

print(m_a)
print(m_b)