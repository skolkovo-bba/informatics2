INF = 1000000000

n, m, s, f = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
	v, u, w = map(int, input().split())
	g[u].append([v, w])
	g[v].append([u, w])

d = [INF] * n
p = [None] * n
d[s] = 0
u = [False] * n;
for i in range(n):
	v = -1
	for j in range(n):
		if (not u[j]) and (v == -1 or d[j] < d[v]):
			v = j
	if d[v] == INF:
		break
	u[v] = True

	for to, l in g[v]:
		if d[v] + l < d[to]:
			d[to] = d[v] + l
			p[to] = v

path = []
v = f
while v != s:
	path.append(v)
	v = p[v]
path.append(s)
print(*path[::-1])