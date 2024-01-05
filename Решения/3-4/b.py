g = [list(map(int, input().split())) for _ in range(int(input()))]
ans1 = set()
ans2 = set()


for i in range(len(g)):
    for j in range(len(g)):
        if g[i][j] == 1:
            if i > j:
                ans1.add((i, j))
            elif i == j:
                pass
            else:
                ans2.add((j, i))

if ans1 == ans2:
    print("YES")
else:
    print("NO")