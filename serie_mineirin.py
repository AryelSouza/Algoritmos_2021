from math import sqrt

def primo(n):
    for y in range(2, int(sqrt(n) + 1)):
        if not n % y:
            return False
    return True
def MDC(dvdndo, dvsor):
    if dvsor == 0:
        return dvdndo
    else:
        return MDC(dvsor, dvdndo % dvsor)
def primentre(x, i):
    if MDC(x, i) == 1:
        return True
    return False

T, N, M = [int(x) for x in input().split(" ")]
A = [N, M]

for u in range(2, T):
    if primo(A[u - 1]):
        result = A[u - 1] * 2
        A.append(result)
    elif primentre(A[u - 1], A[u - 2]):
        result = 2 * (A[u - 1] + A[u - 2]) - 3
        A.append(result)
    else:
        result = A[u - 1] + 1
        A.append(result)
print(" ".join(map(str, A)))