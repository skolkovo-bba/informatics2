m = []

for _ in range(int(input())):
    m.append(list(map(int, input().split())))

def how(num, now=0):
    global m, ans

    if m[num][1] == -1 and m[num][2] == -1:
        if ans < now + m[num][0]:
            ans = now + m[num][0]

        return
    elif m[num][1] != -1 and m[num][2] == -1:
        how(m[num][1], now + m[num][0])
    elif m[num][1] == -1 and m[num][2] != -1:
        how(m[num][2], now + m[num][0])
    else:
        how(m[num][1], now + m[num][0])
        how(m[num][2], now + m[num][0])

ans = 0

how(0)

print(ans)