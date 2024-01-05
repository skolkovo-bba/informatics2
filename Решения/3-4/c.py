import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

def dfs(num):
    global used, ans
    used[num] = 1
    ans.append(num)

    if all(used) and 0 in g[num]:
        print(*ans)
        exit(0)

    for to in g[num]:
        if not used[to]:
            dfs(to)
    
    used[num] = 0
    ans.pop()
            

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

used = [0] * n
ans = []
dfs(0)