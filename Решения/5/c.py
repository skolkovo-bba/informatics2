n, m = map(int, input().split())

g = [[] for _ in range(n)]
used = [False] * n
timer = 0
tin = [0] * n
fup = [0] * n


for _ in range(m):
	f, t, c = map(int, input().split())
	f -= 1
	t -= 1
	g[f].append([t, c])
	g[t].append([f, c])
	

def dfs (v, p = -1):
	global used, tin, fup, timer, ans
	used[v] = True
	tin[v] = timer
	fup[v] = timer
	timer += 1
	for to, l in g[v]:
		if to == p:
			continue
		if used[to]:
			fup[v] = min(fup[v], tin[to])
		else:
			dfs(to, v)
			fup[v] = min(fup[v], fup[to])
			if fup[to] > tin[v]:
				ans = max(ans, l)

def find_bridges():
	global used, timer

	timer = 0
	
	for i in range(n):
		if not used[i]:
			dfs(i)

ans = -1
find_bridges()

print(ans)