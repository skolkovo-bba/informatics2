n = int(input())
m = int(input())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    g[a].append(b)
    g[b].append(a)

start = 0

visited = [False] * n
prev = [None] * n
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start 
            dfs(u, visited, prev, g)
dfs(start, visited, prev, g)

if all(visited):
    print("YES")
else:
    print("NO")