m = []

for _ in range(int(input())):
    m.append(list(map(int, input().split())))

def size(num):
    global m, ans

    if m[num][1] == -1 and m[num][2] == -1:
        return 1
    elif m[num][1] != -1 and m[num][2] == -1:
        s = size(m[num][1])

        if ans < s:
            ans = s
        
        return s + 1
    elif m[num][1] == -1 and m[num][2] != -1:
        s = size(m[num][2])

        if ans < s:
            ans = s
        
        return s + 1
    else:
        left = size(m[num][1])
        right = size(m[num][2])

        if ans < abs(left - right):
            ans = abs(left - right)

        return max(left, right) + 1

ans = 0

size(0)

print(ans)