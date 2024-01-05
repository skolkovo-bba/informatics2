inf = float('+inf')

N, M = map(int, input().split())

A = [[float('+inf')]*N for i in range(N)]

for i in range(N):
    A[i][i] = 0

for i in range(M):
    a, b, w = map(int, input().split())
    A[a][b] = A[b][a] = w

for i in range(N):
    for j in range(N):
        for k in range(N):
            A[j][k] = min(A[j][k], A[j][i] + A[i][k])
    
city = 0
summa = inf

for i in range(N):
    current = sum(A[i])
    if current < summa:
        city = i
        summa = current
print(city)