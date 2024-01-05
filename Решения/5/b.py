from collections import deque

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
ans = [[None] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            ans[i][j] = 0
            q.append((i, j))

def gen(now):
    global n, m
    ans = [
        (now[0] + 1, now[1]),
        (now[0] - 1, now[1]),
        (now[0], now[1] + 1),
        (now[0], now[1] - 1),
    ]

    ret = []

    for a in ans:
        if 0 <= a[0] < n:
            if 0 <= a[1] < m:
                ret.append(a)

    return ret

while len(q) > 0:
    now = q.popleft()
    for v in gen(now):
        if ans[v[0]][v[1]] is None:
            ans[v[0]][v[1]] = ans[now[0]][now[1]] + 1 
            q.append(v)

for i in ans:
    print(*i)