import time

INF = 1000000000

n, m = map(int, input().split())
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    d[a][b] = w
    d[b][a] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min (d[i][j], d[i][k] + d[k][j])

ans = 0
for i in range(n):
    if sum(d[i]) <= sum(d[ans]):
        ans = i

print(ans)