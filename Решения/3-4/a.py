g = [list(map(int, input().split())) for _ in range(int(input()))]
ans = []


for i in range(len(g)):
    for j in range(len(g)):
        if g[i][j] != 0:
            ans.append((i, j, g[i][j]))


for line in ans:
    print(*line)

