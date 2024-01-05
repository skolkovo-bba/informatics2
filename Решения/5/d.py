
import sys

	

n, m = map(int, input().split())

g = [[] for _ in range(n)]
used = [False] * n
timer = 0
tin = [0] * n
fup = [0] * n
ans = set()

for _ in range(m):
	f, t = map(int, input().split())
	f -= 1
	t -= 1
	g[f].append(t)
	g[t].append(f)
	
def dfs(v, p = -1):
	global used, ans, tin, fup, timer
	used[v] = True
	tin[v] = timer
	fup[v] = timer
	timer += 1
	children = 0

	for u in g[v]:
		if u == p:
			continue
		if used[u]:
			fup[v] = min(fup[v],tin[u])
		else:
			dfs(u,v)
			fup[v] = min(fup[v],fup[u])
			if fup[u] >= tin[v] and p != -1:
				ans.add(v+1)
			children += 1
		
	if p == -1 and children > 1:
		ans.add(v + 1)

sys.setrecursionlimit(n + 1000)

ans = set()
for i in range(0, n):
	if not used[i]:
		dfs(i)

ans = sorted(list(ans))

if ans:
	print(*ans)
else:
	print(-1)