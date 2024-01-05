n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    g[a].append(b)
    g[b].append(a)

start = 0

D = [None] * n
D[start] = 0
Q = [start]
Qstart = 0
while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1 
    for v in g[u]: 
        if D[v] is None: 
            D[v] = D[u] + 1 
            Q.append(v)

print(*D, sep = "\n")