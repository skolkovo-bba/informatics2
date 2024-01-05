a = [list(map(int, input().split())) for _ in range(int(input()))]

if all([sum(i) == sum(a[0]) for i in a]):
    need = sum(a[0])
    s = 0
    for i in range(len(a)):
        s += a[i][i]
    if s == need:
        s = 0
        for i in range(len(a)):
            s += a[i][len(a) - 1 - i]
        if s == need:
            for i in range(len(a)):
                if need != sum([a[i][j] for j in range(len(a))]):
                    print("NO")    
                    break 
            else:
                print("YES")
        else:
            print("NO")
    else:
        print("NO")

else:
    print("NO")

