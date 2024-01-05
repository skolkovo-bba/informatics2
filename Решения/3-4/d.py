import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

def dfs(num):
    global used, ans, s, s_min, ans_min
    used[num] = 1
    ans.append(num)

    if all(used):
        

        last = 9999999999999999999
        for to, l in g[num]:
            if to == 0 and l < last:
                last = l
        
        s += last
        if s_min > s:
            s_min = s
            ans_min = ans.copy()
        s -= last

    for to, l in g[num]:
        if not used[to]:
            s += l
            dfs(to)
            s -= l
    
    used[num] = 0
    ans.pop()
            

for _ in range(m):
    a, b, l = map(int, input().split())
    g[a].append((b, l))
    g[b].append((a, l))

used = [0] * n
ans = []
s = 0
ans_min = []
s_min = 99999999999999999999999999999999

#print(g)

dfs(0)

print(s_min)
print(*ans_min)