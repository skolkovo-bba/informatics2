d = {}
for _ in range(int(input())):
    key = input()
    d[key] = d.get(key, 0) + 1


c = [(key, d[key]) for key in d]
c.sort(key=lambda x: x[1])
c.reverse()
for name, n in c:
    print(name)