from pprint import pprint
from collections import deque

n, m = map(int, input().split())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
field = [list(input()) for _ in range(n)]
ans = [[None] * m for _ in range(n)]

q = deque()
q.append(start)
ans[start[0]][start[1]] = 0

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
        if field[v[0]][v[1]] == " " and ans[v[0]][v[1]] is None:
            ans[v[0]][v[1]] = ans[now[0]][now[1]] + 1 
            q.append(v)

if ans[end[0]][end[1]] is None:
    print("INF")
else:
    print(ans[end[0]][end[1]])